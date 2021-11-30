from lw_3.tokens.base_token import BaseToken


class CompositeBaseToken(BaseToken):
    _AVAILABLE_TOKEN_SETS = []
    _PROCESSED = False
    _LEN = None

    @classmethod
    def _prediction_processing(cls):
        if cls._PROCESSED:
            return

        from lw_3.tokens.recursive_composite_base_token import CLS
        cls._AVAILABLE_TOKEN_SETS = [[j if j != CLS else cls for j in i] for i in cls._AVAILABLE_TOKEN_SETS]
        cls._LEN = len(cls._AVAILABLE_TOKEN_SETS)
        cls._PROCESSED = True

    @classmethod
    def needed_len(cls):
        cls._prediction_processing()
        return cls._LEN

    @classmethod
    def parse(cls, tokens: list) -> (BaseToken or None, list,):
        cls._prediction_processing()

        for available_tokens in cls._AVAILABLE_TOKEN_SETS:
            new_tokens_part = []
            remaining_tokens_part = tokens.copy()
            for available_token in available_tokens:
                if not len(remaining_tokens_part):
                    break
                elif available_token == remaining_tokens_part[0].__class__ or available_token == remaining_tokens_part[
                    0]:
                    new_tokens_part.append(remaining_tokens_part[0])
                    remaining_tokens_part = remaining_tokens_part[1:]
                elif available_token in CompositeBaseToken.subclasses():
                    new_token, remaining_tokens_part = available_token.parse(remaining_tokens_part)

                    if not new_token:
                        break

                    from lw_3.tokens.recursive_composite_base_token import RecursiveCompositeBaseToken
                    if available_token in RecursiveCompositeBaseToken.subclasses():
                        pre_new_token = new_token
                        while new_token:
                            pre_new_token = new_token
                            pre_remaining_tokens_part = remaining_tokens_part
                            remaining_tokens_part = [new_token] + remaining_tokens_part
                            new_token, remaining_tokens_part = available_token.parse(remaining_tokens_part)
                        new_token = pre_new_token
                        remaining_tokens_part = pre_remaining_tokens_part

                    new_tokens_part.append(new_token)
                else:
                    break

            if len(new_tokens_part) == len(available_tokens):
                return cls(new_tokens_part), remaining_tokens_part
        return None, tokens

    @classmethod
    def subclasses(cls):
        from lw_3.tokens.recursive_composite_base_token import RecursiveCompositeBaseToken
        classes = set(cls.__subclasses__() + RecursiveCompositeBaseToken.subclasses())
        classes.difference_update({RecursiveCompositeBaseToken})
        return list(classes)

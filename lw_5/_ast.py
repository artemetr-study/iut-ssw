import lw_3.tokens as t


class Ast:
    COMPOSITE_TOKENS = t.CompositeBaseToken.subclasses()
    MAX_LEN = max([i.needed_len() for i in COMPOSITE_TOKENS])
    MIN_LEN = min([i.needed_len() for i in COMPOSITE_TOKENS])

    @classmethod
    def parse(cls, tokens: list):
        # iter = 0
        # print(t.ProgramToken.parse(tokens))
        # while not isinstance(tokens[0], t.ProgramToken):
        #     position = 0
        #     while position < len(tokens) - cls.MIN_LEN:
        #         print(position)
        #         if iter > 10000:
        #             print('Seriosly?')
        #             return tokens
        #         for ct in cls.COMPOSITE_TOKENS:
        #
        #             new_token = ct.parse(tokens[position:position + ct.needed_len()])
        #             print(ct._AVAILABLE_TOKEN_SETS, tokens[position:position + ct.needed_len()])
        #             if new_token:
        #                 print(new_token)
        #                 tokens = tokens[:position] + [new_token] + tokens[position + ct.needed_len():]
        #                 break
        #         position += 1

        return t.ProgramToken.parse(tokens)


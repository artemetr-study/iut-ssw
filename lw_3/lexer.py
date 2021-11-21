import lw_3.tokens as t


class Lexer:
    SIMPLE_TOKENS = t.SimpleToken.__subclasses__()

    @classmethod
    def parse(cls, expression: str):
        tokens = []
        for i in expression:
            token = None
            for st in cls.SIMPLE_TOKENS:
                token = st.parse(i)
                if token:
                    break
            if isinstance(token, t.WhitespaceToken):
                continue
            tokens.append(token)
        return tokens


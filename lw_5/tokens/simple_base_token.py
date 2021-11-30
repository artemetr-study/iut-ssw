from lw_3.tokens.base_token import BaseToken


class SimpleBaseToken(BaseToken):
    _AVAILABLE_SYMBOLS = []

    @classmethod
    def parse(cls, symbol) -> BaseToken or None:
        return cls(symbol) if symbol in cls._AVAILABLE_SYMBOLS else None

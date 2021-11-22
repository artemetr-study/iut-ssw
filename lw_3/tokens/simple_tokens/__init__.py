from lw_3.tokens.simple_base_token import SimpleBaseToken


class RelationSymbolToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = '><='


class ColonToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = ':'


class ArithmeticalSymbolToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = '+-'


class OpeningParenthesisToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = '('


class ClosingParenthesisToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = ')'


class CommaToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = ','


class SemicolonToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = ';'


class WhitespaceToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = ' \n\r\t'


class IdentifierToken(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = 'abcdefghijklnmopqrstuvwxyz'

    @classmethod
    def set_form_string(cls, string):
        return [cls(i) for i in string]


class Digit16Token(SimpleBaseToken):
    _AVAILABLE_SYMBOLS = '0123456789ABCDEF'

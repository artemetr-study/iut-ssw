CLS = 'cls'


class Token:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'<[{self.__class__.__name__}](value=`{self.value}`)>'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and self.value == other.value

    @classmethod
    def parse(cls, symbol):
        pass

    @classmethod
    def subclasses(cls):
        return cls.__subclasses__()


class SimpleToken(Token):
    _AVAILABLE_SYMBOLS = []

    @classmethod
    def parse(cls, symbol) -> Token or None:
        return cls(symbol) if symbol in cls._AVAILABLE_SYMBOLS else None


class CompositeToken(Token):
    _AVAILABLE_TOKEN_SETS = []
    _PROCESSED = False
    _LEN = None

    @classmethod
    def _prediction_processing(cls):
        if cls._PROCESSED:
            return

        cls._AVAILABLE_TOKEN_SETS = [[j if j != CLS else cls for j in i] for i in cls._AVAILABLE_TOKEN_SETS]
        cls._LEN = len(cls._AVAILABLE_TOKEN_SETS)
        cls._PROCESSED = True

    @classmethod
    def needed_len(cls):
        cls._prediction_processing()
        return cls._LEN

    @classmethod
    def parse(cls, tokens: list) -> (Token or None, list,):
        cls._prediction_processing()

        for available_tokens in cls._AVAILABLE_TOKEN_SETS:
            new_tokens_part = []
            remaining_tokens_part = tokens.copy()
            for available_token in available_tokens:
                if not len(remaining_tokens_part):
                    break
                elif available_token == remaining_tokens_part[0].__class__ or available_token == remaining_tokens_part[0]:
                    new_tokens_part.append(remaining_tokens_part[0])
                    remaining_tokens_part = remaining_tokens_part[1:]
                elif available_token in CompositeToken.subclasses():
                    new_token, remaining_tokens_part = available_token.parse(remaining_tokens_part)

                    if not new_token:
                        break

                    if available_token in RecursiveCompositeToken.subclasses():
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
        classes = set(cls.__subclasses__() + RecursiveCompositeToken.subclasses())
        classes.difference_update({RecursiveCompositeToken})
        return list(classes)


class RecursiveCompositeToken(CompositeToken):
    @classmethod
    def subclasses(cls):
        return cls.__subclasses__()


class RelationSymbolToken(SimpleToken):
    _AVAILABLE_SYMBOLS = '><='


class ColonToken(SimpleToken):
    _AVAILABLE_SYMBOLS = ':'


class EqualOperationSymbolToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[ColonToken, RelationSymbolToken('=')]]


class ArithmeticalSymbolToken(SimpleToken):
    _AVAILABLE_SYMBOLS = '+-'


class OpeningParenthesisToken(SimpleToken):
    _AVAILABLE_SYMBOLS = '('


class ClosingParenthesisToken(SimpleToken):
    _AVAILABLE_SYMBOLS = ')'


class CommaToken(SimpleToken):
    _AVAILABLE_SYMBOLS = ','


class SemicolonToken(SimpleToken):
    _AVAILABLE_SYMBOLS = ';'


class WhitespaceToken(SimpleToken):
    _AVAILABLE_SYMBOLS = ' \n\r\t'


class IdentifierToken(SimpleToken):
    _AVAILABLE_SYMBOLS = 'abcdefghijklnmopqrstuvwxyz'

    @classmethod
    def set_form_string(cls, string):
        return [cls(i) for i in string]


class ReadLnToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('readln')]


class Digit16Token(SimpleToken):
    _AVAILABLE_SYMBOLS = '0123456789ABCDEF'


class IdentifierListToken(RecursiveCompositeToken):
    _AVAILABLE_TOKEN_SETS = [[IdentifierToken], [CLS, CommaToken, IdentifierToken]]


class InputOperatorToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[ReadLnToken, OpeningParenthesisToken, IdentifierListToken, ClosingParenthesisToken]]


class IfToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('if')]


class ThenToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('then')]


class ElseToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('else')]


class CaseToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('case')]


class OfToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('of')]


class EndToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('end')]


class RepeatToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('repeat')]


class UntilToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('until')]


class WhileToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('while')]


class DoToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('do')]


class BeginToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('begin')]


class ForToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('for')]


class ToToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('to')]


class VarToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('var')]


class DigitToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[Digit16Token]]


class ConstantToken(RecursiveCompositeToken):
    _AVAILABLE_TOKEN_SETS = [[DigitToken], [DigitToken, CLS]]


class OperandToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[IdentifierToken], [ConstantToken]]


class ConditionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[OperandToken], [RelationSymbolToken, OperandToken]]


class OrToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('or')]


class AndToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('and')]


class ShlToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('shl')]


class ShrToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('shr')]


class OperationSymbolToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[ArithmeticalSymbolToken], [OrToken], [AndToken], [ShrToken], [ShlToken]]


class ArithmeticalOrLogicalExpressionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[OperandToken, OperationSymbolToken, OperandToken], [OperandToken]]


class EqualOperatorToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[IdentifierToken, EqualOperationSymbolToken, ArithmeticalOrLogicalExpressionToken]]


class CaseListToken(RecursiveCompositeToken):
    _AVAILABLE_TOKEN_SETS = [[ConstantToken, ColonToken, EqualOperatorToken],
                             [CLS, ColonToken, ConstantToken, CommaToken, EqualOperatorToken]]


class CaseConstructionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[CaseToken, IdentifierToken, OfToken, CaseListToken, EndToken]]


class EqListToken(RecursiveCompositeToken):
    _AVAILABLE_TOKEN_SETS = [[EqualOperatorToken], [CLS, SemicolonToken, EqualOperatorToken]]


class ForConstructionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [
        [ForToken, EqualOperatorToken, ToToken, OperandToken, DoToken, BeginToken, EqListToken, EndToken]]


class WhileConstructionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[WhileToken, ConditionToken, DoToken, BeginToken, EqListToken, EndToken]]


class RepeatConstructionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[RepeatToken, EqListToken, UntilToken, ConditionToken]]


class IfConstructionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[IfToken, ConditionToken, ThenToken, EqualOperatorToken, ElseToken, EqualOperatorToken]]


class ControlConstructionToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[IfConstructionToken], [ForConstructionToken], [WhileConstructionToken],
                             [RepeatConstructionToken], [CaseConstructionToken]]


class OperatorToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[EqualOperatorToken], [InputOperatorToken], [ControlConstructionToken]]


class OperatorListToken(RecursiveCompositeToken):
    _AVAILABLE_TOKEN_SETS = [[OperatorToken], [CLS, OperatorToken]]


class ProgramToken(CompositeToken):
    _AVAILABLE_TOKEN_SETS = [[VarToken, IdentifierListToken, BeginToken, OperatorListToken, EndToken]]

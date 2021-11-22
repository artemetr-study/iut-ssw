from lw_3.tokens.composite_base_token import CompositeBaseToken
from lw_3.tokens.recursive_composite_base_token import RecursiveCompositeBaseToken, CLS
from lw_3.tokens.simple_tokens import IdentifierToken, Digit16Token, RelationSymbolToken, ArithmeticalSymbolToken, \
    ColonToken, CommaToken, SemicolonToken, OpeningParenthesisToken, ClosingParenthesisToken


class EqualOperationSymbolToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[ColonToken, RelationSymbolToken('=')]]


class ReadLnToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('readln')]


class WriteLnToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('writeln')]


class IdentifierListToken(RecursiveCompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[IdentifierToken], [CLS, CommaToken, IdentifierToken]]


class InputOperatorToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[ReadLnToken, OpeningParenthesisToken, IdentifierListToken, ClosingParenthesisToken]]


class OutputOperatorToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[WriteLnToken, OpeningParenthesisToken, IdentifierListToken, ClosingParenthesisToken]]


class IfToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('if')]


class ThenToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('then')]


class ElseToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('else')]


class CaseToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('case')]


class OfToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('of')]


class EndToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('end')]


class RepeatToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('repeat')]


class UntilToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('until')]


class WhileToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('while')]


class DoToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('do')]


class BeginToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('begin')]


class ForToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('for')]


class ToToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('to')]


class VarToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('var')]


class DigitToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[Digit16Token]]


class ConstantToken(RecursiveCompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[DigitToken], [DigitToken, CLS]]


class OperandToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[IdentifierToken], [ConstantToken]]


class ConditionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[OperandToken], [RelationSymbolToken, OperandToken]]


class OrToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('or')]


class AndToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('and')]


class ShlToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('shl')]


class ShrToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [IdentifierToken.set_form_string('shr')]


class OperationSymbolToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[ArithmeticalSymbolToken], [OrToken], [AndToken], [ShrToken], [ShlToken]]


class ArithmeticalOrLogicalExpressionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[OperandToken, OperationSymbolToken, OperandToken], [OperandToken]]


class EqualOperatorToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[IdentifierToken, EqualOperationSymbolToken, ArithmeticalOrLogicalExpressionToken]]


class CaseListToken(RecursiveCompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[ConstantToken, ColonToken, EqualOperatorToken],
                             [CLS, CommaToken, ConstantToken, ColonToken, EqualOperatorToken]]


class CaseConstructionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[CaseToken, IdentifierToken, OfToken, CaseListToken, EndToken]]


class EqListToken(RecursiveCompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[EqualOperatorToken], [CLS, SemicolonToken, EqualOperatorToken]]


class ForConstructionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [
        [ForToken, EqualOperatorToken, ToToken, OperandToken, DoToken, BeginToken, EqListToken, EndToken]]


class WhileConstructionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[WhileToken, ConditionToken, DoToken, BeginToken, EqListToken, EndToken]]


class RepeatConstructionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[RepeatToken, EqListToken, UntilToken, ConditionToken]]


class IfConstructionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[IfToken, ConditionToken, ThenToken, EqualOperatorToken, ElseToken, EqualOperatorToken]]


class ControlConstructionToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[IfConstructionToken], [ForConstructionToken], [WhileConstructionToken],
                             [RepeatConstructionToken], [CaseConstructionToken]]


class OperatorToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[EqualOperatorToken], [InputOperatorToken], [OutputOperatorToken],
                             [ControlConstructionToken]]


class OperatorListToken(RecursiveCompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[OperatorToken], [CLS, OperatorToken]]


class ProgramToken(CompositeBaseToken):
    _AVAILABLE_TOKEN_SETS = [[VarToken, IdentifierListToken, BeginToken, OperatorListToken, EndToken]]

import re


class ReversePolishNotationException(Exception):
    @staticmethod
    def build_unopened_bracket_message(expr: str):
        return f'Unopened bracket: `{expr}`'

    @classmethod
    def unopened_bracket(cls, expression):
        raise cls(cls.build_unopened_bracket_message(expression))


class ReversePolishNotation:
    _OPERATORS_PRIORITY = {
        '(': 0,
        '=': 1,
        '+': 2,
        '-': 2,
        '*': 3,
        '/': 3,
    }

    def __init__(self):
        self._expression = ''
        self._operators = []
        self._result = []

    def __str__(self):
        return ' '.join(self._result)

    @classmethod
    def _get_operation_priority(cls, operation: str) -> int or None:
        return cls._OPERATORS_PRIORITY.get(operation)

    @staticmethod
    def _expression_parts(expression: str or list) -> str:
        if type(expression) is str:
            expression = re.findall(r'[+\-*/=()]|[\d.z]+|[a-zA-Z]+', re.sub(r'[^\d+\-*/=()a-zA-Z.]', '', expression))
        for part in expression:
            yield part

    @classmethod
    def _expression_generator(cls, expression: str or list) -> (int, str,):
        for part in cls._expression_parts(expression):
            yield cls._get_operation_priority(part), part

    def _from_expression(self, expression: str or list):
        self._expression = expression
        for priority, part in self._expression_generator(self._expression):
            if priority is None:
                if part == ')':
                    if '(' not in self._operators:
                        raise ReversePolishNotationException.unopened_bracket(expression)

                    operator = self._operators.pop()
                    while operator != '(':
                        self._result.append(operator)
                        operator = self._operators.pop()
                else:
                    self._result.append(part)
            elif not priority or not self._operators or priority > self._get_operation_priority(self._operators[-1]):
                self._operators.append(part)
            elif priority <= self._get_operation_priority(self._operators[-1]):
                while self._operators and self._get_operation_priority(self._operators[-1]) >= priority:
                    self._result.append(self._operators.pop())
                self._operators.append(part)

        while self._operators:
            self._result.append(self._operators.pop())

        return self

    @classmethod
    def from_expression(cls, expression: str or list):
        return cls()._from_expression(expression)

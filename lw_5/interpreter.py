from lw_3.tokens import BaseToken, IdentifierListToken, IdentifierToken, OperatorToken, \
    InputOperatorToken, OutputOperatorToken, EqualOperatorToken, ArithmeticalSymbolToken, OrToken, AndToken, ShrToken, \
    ShlToken, OperandToken, ArithmeticalOrLogicalExpressionToken, ConstantToken, CaseConstructionToken, CaseListToken, \
    CompositeBaseToken


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.arithm_cache = {}

    def has_var(self, name) -> bool:
        return name in self.vars.keys()

    def define_var(self, name):
        if self.has_var(name):
            raise Exception(f'Variable {name} is already defined')

        self.vars[name] = None

    def get_var(self, name):
        if not self.has_var(name):
            raise Exception(f'Variable {name} is not defined')

        return self.vars[name]

    def drop_cache(self, name):
        for k in list(self.arithm_cache.keys()):
            if name in k:
                print(f'Удаляю кэш для переменных содержащих {name}')
                del self.arithm_cache[k]

    def set_var(self, name, value):
        if not self.has_var(name):
            raise Exception(f'Variable {name} is not defined')

        if self.vars[name] != value:
            self.drop_cache(name)

        self.vars[name] = value

    def get_constant_value(self, token: ConstantToken, first=True):
        result = token.value[0].value[0].value
        if len(token.value) > 1:
            result += self.get_constant_value(token.value[1], first=False)
        if first:
            result = int(result, 16)
        return result

    def get_operand_value(self, token: OperandToken):
        if token.value[0].__class__ == IdentifierToken:
            return self.get_var(token.value[0].value)
        elif token.value[0].__class__ == ConstantToken:
            return self.get_constant_value(token.value[0])
        else:
            raise Exception('Undefined token')

    def arithmetical_or_logical_expression_exec(self, token: ArithmeticalOrLogicalExpressionToken):
        key = {hash(token.__str__())}
        if token.value[0].value[0].__class__ == IdentifierToken:
            key.add(token.value[0].value[0].value)

        if len(token.value) == 3 and token.value[2].value[0].__class__ == IdentifierToken:
            key.add(token.value[2].value[0].value)

        key = frozenset(key)
        if self.arithm_cache.get(key) is not None:
            print(f'Тут есть кэш для {key}')
            return self.arithm_cache[key]

        operations = {
            ArithmeticalSymbolToken.__name__: lambda a, b, operator: a + b if operator == '+' else a - b,
            OrToken.__name__: lambda a, b, _: a or b,
            AndToken.__name__: lambda a, b, _: a and b,
            ShrToken.__name__: lambda a, b, _: a >> b,
            ShlToken.__name__: lambda a, b, _: a << b,
        }
        if len(token.value) == 3:
            result = operations[token.value[1].value[0].__class__.__name__](self.get_operand_value(token.value[0]),
                                                                            self.get_operand_value(token.value[2]),
                                                                            token.value[1].value[0].value)
        else:
            result = self.get_operand_value(token.value[0])

        self.arithm_cache[key] = result
        print(f'Назначили кэш для {key}')
        return result

    def get_cases_by_case_list_token(self, case_list: CaseListToken):
        if case_list.value[0].__class__ == CaseListToken:
            result = self.get_cases_by_case_list_token(case_list.value[0])
            result[self.get_constant_value(case_list.value[2])] = case_list.value[4]
        else:
            result = {
                self.get_constant_value(case_list.value[0]): case_list.value[2]
            }

        return result

    def execute(self, token: BaseToken):
        if token.__class__ == IdentifierListToken:
            for sub_token in token.value:
                if sub_token.__class__ == IdentifierListToken:
                    self.execute(sub_token)
                if sub_token.__class__ == IdentifierToken:
                    self.define_var(sub_token.value)
        elif token.__class__ == OperatorToken:
            self.execute(token.value[0])
        elif token.__class__ == InputOperatorToken:
            for i in token.value[2].get_all_identifiers():
                self.set_var(i.value, int(input(), 16))
        elif token.__class__ == OutputOperatorToken:
            for i in token.value[2].get_all_identifiers():
                print(hex(self.get_var(i.value)))
        elif token.__class__ == EqualOperatorToken:
            self.drop_cache(token.value[0].value)
            self.set_var(token.value[0].value, self.arithmetical_or_logical_expression_exec(token.value[2]))
        elif token.__class__ == CaseConstructionToken:
            identifier = token.value[1].value
            identifier_value = self.get_var(identifier)
            cases = self.get_cases_by_case_list_token(token.value[3])
            if cases.get(identifier_value):
                self.execute(cases[identifier_value])
        else:
            if token.__class__ in CompositeBaseToken.subclasses():
                for i in token.value:
                    if i.__class__ in CompositeBaseToken.subclasses():
                        self.execute(i)

from lw_3.lexer import Lexer
from lw_3._ast import Ast
from lw_3.interpreter import Interpreter

if __name__ == '__main__':
    with open('pc.p') as f:
        text = f.read()

    lexems = Lexer.parse(text)

    # print('\n'.join([f'{i.value}\t{i.__class__.__name__}' for i in lexems]))
    # exit()
    program, _ = Ast.parse(lexems)
    # print(program)
    # exit()

    interpreter = Interpreter()
    interpreter.execute(program)


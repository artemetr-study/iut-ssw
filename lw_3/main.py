from lw_3.lexer import Lexer
from lw_3._ast import Ast

if __name__ == '__main__':
    with open('pc.p') as f:
        text = f.read()

    lexems = Lexer.parse(text)
    # print('\n'.join([f'{i.value}\t{i.__class__.__name__}' for i in lexems]))
    print(Ast.parse(lexems))
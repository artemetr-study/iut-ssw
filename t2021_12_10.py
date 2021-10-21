"""
Задание. Построить грамматику для языка, предложениями которого являются цепочки длиной 2 байта,
в которых на пятой позиции справа стоит 1. Входной алфавит {0, 1}.
"""
import re


class T:
    a = lambda x: x == '0'
    b = lambda x: x == '1'


class N:
    @classmethod
    def A(cls, x):
        """
        A -> a|b
        """
        return T.a(x) or T.b(x)

    @classmethod
    def B(cls, x):
        """
        B -> AB|A
        """
        return (T.a(x[0]) or T.b(x[0])) and (len(x) == 1 or cls.B(x[1:]))


def S(x):
    return len(x) == 16 and N.B(x[:11]) and T.b(x[11]) and N.B(x[12:16])


if __name__ == '__main__':
    print(S('1000111001110101'))
    print(bool(re.findall(r'^[01]{11}1[01]{4}$', '0000111001110101')))

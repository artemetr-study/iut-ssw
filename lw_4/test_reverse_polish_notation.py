import unittest

from lw_4.reverse_polish_notation import ReversePolishNotation, ReversePolishNotationException


class ReversePolishNotationTestCase(unittest.TestCase):
    def test_default_only_literal_string_expression(self):
        expression, excepted_expression = 'a+b+b-s*t=c', 'a b + b + s t * - c ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_default_only_literal_list_expression(self):
        expression, excepted_expression = ['a', '+', 'b', '+', 'b', '-', 's', '*', 't', '=',
                                           'c'], 'a b + b + s t * - c ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_default_only_numeric_string_expression(self):
        expression, excepted_expression = '12+13+13-1*2=36', '12 13 + 13 + 1 2 * - 36 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_default_only_numeric_list_expression(self):
        expression, excepted_expression = ['12', '+', '13', '+', '13', '-', '1', '*', '2', '=',
                                           '36'], '12 13 + 13 + 1 2 * - 36 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_default_only_float_string_expression(self):
        expression, excepted_expression = '12.0+13.000+13.0-1*2=36', '12.0 13.000 + 13.0 + 1 2 * - 36 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_default_only_float_list_expression(self):
        expression, excepted_expression = ['12.0', '+', '13.000', '+', '13.0', '-', '1', '*', '2', '=',
                                           '36'], '12.0 13.000 + 13.0 + 1 2 * - 36 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_invalid_default_only_float_string_expression(self):
        pass

    def test_invalid_default_only_float_list_expression(self):
        pass

    def test_brackets_only_float_string_expression(self):
        expression, excepted_expression = '12.0+(13.000+13.0-1)*2=36', '12.0 13.000 13.0 + 1 - 2 * + 36 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_brackets_only_float_list_expression(self):
        expression, excepted_expression = ['12.0', '+', '(', '13.000', '+', '13.0', '-', '1', ')', '*', '2', '=',
                                           '36'], '12.0 13.000 13.0 + 1 - 2 * + 36 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_unopened_bracket_exception(self):
        self.assertRaises(ReversePolishNotationException, ReversePolishNotation.from_expression,
                          'r/(2/(b-c+d))*f)-e*l=a*(2-3+4*8-2/1)')

    def test_1(self):
        expression, excepted_expression = '(f+g-k)*2*(a+b-d/c*d)=a/d*c-f', 'f g + k - 2 * a b + d c / d * - * a d / c * f - ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_2(self):
        expression, excepted_expression = 't+l-p*(5-6+y)/5=1/2*(f-g+j)', 't l + p 5 6 - y + * 5 / - 1 2 / f g - j + * ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_3(self):
        expression, excepted_expression = '(a-d/(2*(b-c+d))*f)e=a+a/5*6', 'a d 2 b c - d + * / f * - e a a 5 / 6 * + ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_4(self):
        expression, excepted_expression = '(((a+b)/2*e)a*(a+b)*2)/2=0', 'a b + 2 / e * a a b + * 2 * 2 / 0 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_5(self):
        expression, excepted_expression = '2+(a-b)*2/(a-b)*2=(a-b)*2', '2 a b - 2 * a b - / 2 * + a b - 2 * ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_6(self):
        expression, excepted_expression = 'y*(2-(3+4-5)*8)-2/1*8=(a-b+c*2)/1*(a+b)', 'y 2 3 4 + 5 - 8 * - * 2 1 / 8 * - a b - c 2 * + 1 / a b + * ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_7(self):
        expression, excepted_expression = '2*3/1+(1+1-0)/(a+a)=((a-b)*(a+b))/2*4', '2 3 * 1 / 1 1 + 0 - a a + / + a b - a b + * 2 / 4 * ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_8(self):
        expression, excepted_expression = '(l-k+h)/(g-h+k)*4=g*h/k*p/(a+s)', 'l k - h + g h - k + / 4 * g h * k / p * a s + / ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_9(self):
        expression, excepted_expression = 'r/((g-h+k)*(a+s-d))*f=g*(a-s)-l', 'r g h - k + a s + d - * / f * g a s - * l - ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_10(self):
        expression, excepted_expression = 'e-(f+g*h)/r-f/(d-f)=(4-2+7*8)/5', 'e f g h * + r / - f d f - / - 4 2 - 7 8 * + 5 / ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_11(self):
        expression, excepted_expression = 'a+(s-d+f)*i-g+h-j+k=w*e/r*t/y', 'a s d - f + i * + g - h + j - k + w e * r / t * y / ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_12(self):
        expression, excepted_expression = 't*(a-p*d/(2/(b-c+d))*f)e*l=a', 't a p d * 2 b c - d + / / f * - e * l * a ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_13(self):
        expression, excepted_expression = '(q/(w+e)-q*(w-e))*(q/(w+e)-q*(w-e))=0', 'q w e + / q w e - * - q w e + / q w e - * - * 0 ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_14(self):
        expression, excepted_expression = 'f/(a-b)*2=r/((g-h+k)*(a+s-d))*f*g', 'f a b - / 2 * r g h - k + a s + d - * / f * g * ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_15(self):
        expression, excepted_expression = '((l-k+h)/(g-h+k)*4)/p=d-2*(a+b-d/c*d)', 'l k - h + g h - k + / 4 * p / d 2 a b + d c / d * - * - ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_16(self):
        expression, excepted_expression = 'f*(2+a-b)*2/(a-b)*2=(a-b)*2/1', 'f 2 a + b - * 2 * a b - / 2 * a b - 2 * 1 / ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_17(self):
        expression, excepted_expression = 'q*(w/(e-f+g)-(j-t+r))-(f-g+h-j)*6=6+5-4', 'q w e f - g + / j t - r + - * f g - h + j - 6 * - 6 5 + 4 - ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_18(self):
        expression, excepted_expression = 'a*(a+b)*2/2-(a-b)*(a+b)=(a-b)*2', 'a a b + * 2 * 2 / a b - a b + * - a b - 2 * ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_19(self):
        expression, excepted_expression = '3*((r-y)*(b-c+d))*f=k+h/(g-h+k)*4', '3 r y - b c - d + * * f * k h g h - k + / 4 * + ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)

    def test_20(self):
        expression, excepted_expression = '(r/(2/(b-c+d))*f)-e*l=a*(2-3+4*8-2/1)', 'r 2 b c - d + / / f * e l * - a 2 3 - 4 8 * + 2 1 / - * ='
        self.assertEqual(str(ReversePolishNotation.from_expression(expression)), excepted_expression)


if __name__ == '__main__':
    unittest.main()

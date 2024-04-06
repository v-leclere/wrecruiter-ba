import unittest

from app.rpn.calculator import Calculator


def resolve(expression):
    calculator = Calculator()

    return float(calculator.resolve(expression))


class TestCalculatorMethods(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(resolve("8 7 +"), 15.0)
        self.assertEqual(resolve("4 7 *"), 28.0)
        self.assertEqual(resolve("8 3 -"), 5.0)
        self.assertEqual(resolve("36 9 /"), 4.0)

    def test_advanced(self):
        self.assertEqual(resolve("99 11 + 8 7 + +"), 125.0)
        self.assertEqual(resolve("4 7 * 5 2 * *"), 280.0)
        self.assertEqual(resolve("33 3 - 10 6 - -"), 26.0)
        self.assertEqual(resolve("90 3 / 30 5 / /"), 5.0)
        self.assertEqual(resolve("15 7 1 1 + - / 3 * 2 1 1 + + -"), 5.0)

    def test_float(self):
        self.assertEqual(resolve("1.2 2 *"), 2.4)


if __name__ == '__main__':
    unittest.main()

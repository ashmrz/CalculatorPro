import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_constructor(self):
        name = 'ماشین حساب'
        calculator = Calculator(name)
        self.assertEqual(calculator.name, name)

        name = 'Ashkan'
        calculator = Calculator(name)
        self.assertEqual(calculator.name, name)

    def test_add(self):
        name = 'Calc'
        calculator = Calculator(name)
        self.assertEqual(calculator.compute_add(10, 20), 30)
        self.assertAlmostEqual(calculator.compute_add(-5, 0.2), -4.8)
        self.assertAlmostEqual(calculator.compute_add(10, -8.7), 1.3)

    def test_sub(self):
        name = 'Calc'
        calculator = Calculator(name)
        self.assertEqual(calculator.compute_sub(2, 10), -8)
        self.assertAlmostEqual(calculator.compute_sub(-1, 0.5), -1.5)

    def test_div(self):
        name = 'Calc'
        calculator = Calculator(name)
        self.assertEqual(calculator.compute_div(4, -2), -2)
        self.assertEqual(calculator.compute_div(4, 0), Errors.DIV_BY_ZERO)
        self.assertAlmostEqual(calculator.compute_div(5, 2), 2.5)

    def test_mul(self):
        name = 'Calc'
        calculator = Calculator(name)
        self.assertEqual(calculator.compute_mul(2, 10), 20)
        self.assertAlmostEqual(calculator.compute_mul(-2, 0.3), -0.6)

    def test_sqrt(self):
        name = 'Calc'
        calculator = Calculator(name)
        self.assertEqual(calculator.compute_sqrt(4), 2)
        self.assertEqual(calculator.compute_sqrt(9), 3)
        self.assertEqual(calculator.compute_sqrt(25), 5)
        self.assertEqual(calculator.compute_sqrt(36), 6)
        self.assertEqual(calculator.compute_sqrt(-10), Errors.NEGATIVE_SQRT)

    def test_pow(self):
        name = 'Calc'
        calculator = Calculator(name)
        self.assertEqual(calculator.compute_pow(2, 10), 1024)
        self.assertAlmostEqual(calculator.compute_pow(5, 3), 125)

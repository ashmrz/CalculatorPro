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

    def test_mul(self):
        name = 'Calc'
        calculator = Calculator(name)
        self.assertEqual(calculator.compute_mul(2, 10), 20)
        self.assertAlmostEqual(calculator.compute_mul(-2, 0.3), -0.6)

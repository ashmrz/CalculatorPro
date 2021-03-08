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
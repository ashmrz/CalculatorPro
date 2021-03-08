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

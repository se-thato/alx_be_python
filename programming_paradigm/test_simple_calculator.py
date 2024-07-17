import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCazlculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(4, 6), 10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(20, 5), 15)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def division(self):
        self.assertEqual(self.calc.divide(5, 0), None)
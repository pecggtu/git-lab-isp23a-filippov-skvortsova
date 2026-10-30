import unittest
from main import add, subtract, multiply, modulo, calculate

class CalculatorTests(unittest.TestCase):
    def test_add(self): self.assertEqual(add(2, 3), 5)
    def test_subtract(self): self.assertEqual(subtract(2, 3), -1)
    def test_multiply(self): self.assertEqual(multiply(-2, 3), -6)
    def test_modulo(self): self.assertEqual(modulo(7, 3), 1)
    def test_modulo_negative(self): self.assertEqual(modulo(-7, 3), 2)
    def test_modulo_zero(self):
        with self.assertRaises(ZeroDivisionError): modulo(7, 0)
    def test_dispatch_add(self): self.assertEqual(calculate(2, 3, "+"), 5)
    def test_dispatch_subtract(self): self.assertEqual(calculate(2, 3, "-"), -1)
    def test_bad_type(self):
        with self.assertRaises(TypeError): calculate("2", 3, "+")
    def test_bad_operation(self):
        with self.assertRaises(ValueError): calculate(2, 3, "?")

if __name__ == "__main__": unittest.main()

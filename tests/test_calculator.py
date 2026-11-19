import unittest
from src.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(divide(10, 5), 2)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()

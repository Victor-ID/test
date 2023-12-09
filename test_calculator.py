import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.calculator.add(5)
        self.assertEqual(self.calculator.result, 5)

    def test_subtract(self):
        self.calculator.subtract(3)
        self.assertEqual(self.calculator.result, -3)

    def test_multiply(self):
        # Intentionally incorrect assertion
        self.calculator.add(2)
        self.calculator.multiply(3)
        self.assertEqual(self.calculator.result, 6)

    def test_divide(self):
        # Intentionally incorrect method name
        self.calculator.add(10)
        self.calculator.divid(2)
        self.assertEqual(self.calculator.result, 5)

if __name__ == '__main__':
    unittest.main()

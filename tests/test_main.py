# tests/test_main.py

import unittest
from app.main import add, subtract

class TestMathFunctions(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)

if __name__ == '__main__':
    unittest.main()

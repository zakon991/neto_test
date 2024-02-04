import unittest
from main_task3 import discriminant
class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant(self):
        self.assertEqual(discriminant(1, 8, 15), 4)
        self.assertEqual(discriminant(1, -13, 12), 121)
        self.assertEqual(discriminant(-4, 28, -49), 0)
        self.assertEqual(discriminant(1, 1, 1), -3)

if __name__ == '__main__':
    unittest.main()

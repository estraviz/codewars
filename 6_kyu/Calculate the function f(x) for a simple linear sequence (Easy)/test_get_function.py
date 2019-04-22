import unittest
from get_function import get_function


class TestGetFunction(unittest.TestCase):

    def test_linear_with_zero_y_intercept(self):
        self.assertEqual(get_function([0, 1, 2, 3, 4]), "f(x) = x")
        self.assertEqual(get_function([0, 3, 6, 9, 12]), "f(x) = 3x")

    def test_linear_with_slope_and_y_intercept(self):
        self.assertEqual(get_function([1, 4, 7, 10, 13]), "f(x) = 3x + 1")
        self.assertEqual(get_function([3, -1, -5, -9, -13]), "f(x) = -4x + 3")
        self.assertEqual(get_function([-1, -5, -9, -13, -17]),
                         "f(x) = -4x - 1")

    def test_no_linear_sequence(self):
        self.assertEqual(get_function([-1, -888, 768546, -13, -456546]),
                         "Non-linear sequence")
        self.assertEqual(get_function([1, 2, 4, 7, 11]), "Non-linear sequence")

    def test_constant_relationship(self):
        self.assertEqual(get_function([3, 3,  3, 3, 3]), "f(x) = 3")


if __name__ == '__main__':
    unittest.main()

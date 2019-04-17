import unittest
from calc import calc


class TextFindEvenIndex(unittest.TestCase):

    def test_duplicate_count(self):
        self.assertEqual(calc(""), 0)
        self.assertEqual(calc("3"), 3)
        self.assertEqual(calc("3.5"), 3.5)
        self.assertEqual(calc("1 3 +"), 4)
        self.assertEqual(calc("1 3 *"), 3)
        self.assertEqual(calc("1 3 -"), -2)
        self.assertEqual(calc("4 2 /"), 2)
        self.assertEqual(calc("10000 123 +"), 10123)
        self.assertEqual(calc("5 1 2 + 4 * + 3 -"), 14)


if __name__ == '__main__':
    unittest.main()

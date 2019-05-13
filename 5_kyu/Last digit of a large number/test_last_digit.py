import unittest
from last_digit import last_digit


class TestLastDigit(unittest.TestCase):

    def test_last_digits(self):
        self.assertEqual(last_digit(4, 1), 4)
        self.assertEqual(last_digit(4, 2), 6)
        self.assertEqual(last_digit(9, 7), 9)
        self.assertEqual(last_digit(10, 1000000000), 0)

        a = 38710248912497124917933333333284108412048102948908149081409204712406
        b = 226628148126342643123641923461846128214626
        self.assertEqual(last_digit(a, b), 6)

        a = 3715290469715693021198967285016729344580685479654510946723
        b = 68819615221552997273737174557165657483427362207517952651
        self.assertEqual(last_digit(a, b), 7)


if __name__ == '__main__':
    unittest.main()

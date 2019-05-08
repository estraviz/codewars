import unittest
from dig_pow import dig_pow


class TestDigPow(unittest.TestCase):

    def test_dig_pow(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(46288, 3), 51)
        self.assertEqual(dig_pow(114, 3), 9)
        self.assertEqual(dig_pow(46288, 5), -1)
        self.assertEqual(dig_pow(135, 1), 1)
        self.assertEqual(dig_pow(175, 1), 1)
        self.assertEqual(dig_pow(518, 1), 1)
        self.assertEqual(dig_pow(598, 1), 1)
        self.assertEqual(dig_pow(1306, 1), 1)
        self.assertEqual(dig_pow(2427, 1), 1)
        self.assertEqual(dig_pow(2646798, 1), 1)
        self.assertEqual(dig_pow(3456789, 1), -1)
        self.assertEqual(dig_pow(3456789, 5), -1)
        self.assertEqual(dig_pow(198, 1), 3)
        self.assertEqual(dig_pow(249, 1), 3)
        self.assertEqual(dig_pow(1377, 1), 2)
        self.assertEqual(dig_pow(1676, 1), 1)
        self.assertEqual(dig_pow(695, 2), 2)
        self.assertEqual(dig_pow(1878, 2), 19)
        self.assertEqual(dig_pow(7388, 2), 5)
        self.assertEqual(dig_pow(47016, 2), 1)
        self.assertEqual(dig_pow(542186, 2), 1)
        self.assertEqual(dig_pow(261, 3), 5)
        self.assertEqual(dig_pow(1385, 3), 35)
        self.assertEqual(dig_pow(2697, 3), 66)
        self.assertEqual(dig_pow(6376, 3), 10)
        self.assertEqual(dig_pow(6714, 3), 1)
        self.assertEqual(dig_pow(63760, 3), 1)
        self.assertEqual(dig_pow(63761, 3), 1)
        self.assertEqual(dig_pow(132921, 3), 4)
        self.assertEqual(dig_pow(10383, 6), 12933)


if __name__ == '__main__':
    unittest.main()

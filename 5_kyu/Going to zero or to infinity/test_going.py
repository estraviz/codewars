import unittest
from going import going


class TestGoing(unittest.TestCase):

    def test_going_to_zero_or_to_infinity(self):
        self.assertEqual(going(5), 1.275)
        self.assertEqual(going(6), 1.2125)
        self.assertEqual(going(7), 1.173214)
        self.assertEqual(going(8), 1.146651)
        self.assertEqual(going(20), 1.052786)
        self.assertEqual(going(30), 1.034525)
        self.assertEqual(going(50), 1.020416)
        self.assertEqual(going(113), 1.008929)
        self.assertEqual(going(200), 1.005025)
        self.assertEqual(going(523), 1.001915)
        self.assertEqual(going(1011), 1.00099)
        self.assertEqual(going(10110), 1.000098)


if __name__ == '__main__':
    unittest.main()

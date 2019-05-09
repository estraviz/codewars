import unittest
from series_sum import series_sum


class TestSeriesSum(unittest.TestCase):

    def test_series_sum(self):
        self.assertEqual(series_sum(1), "1.00")
        self.assertEqual(series_sum(2), "1.25")
        self.assertEqual(series_sum(3), "1.39")
        self.assertEqual(series_sum(4), "1.49")
        self.assertEqual(series_sum(5), "1.57")
        self.assertEqual(series_sum(6), "1.63")
        self.assertEqual(series_sum(7), "1.68")
        self.assertEqual(series_sum(8), "1.73")
        self.assertEqual(series_sum(9), "1.77")
        self.assertEqual(series_sum(15), "1.94")
        self.assertEqual(series_sum(39), "2.26")
        self.assertEqual(series_sum(58), "2.40")
        self.assertEqual(series_sum(0), "0.00")


if __name__ == '__main__':
    unittest.main()

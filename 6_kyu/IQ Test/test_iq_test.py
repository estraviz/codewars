import unittest
from iq_test import iq_test


class TestIQTest(unittest.TestCase):

    def test_iq_test(self):
        s = "2 4 7 8 10"
        self.assertEqual(iq_test(s), 3)

        s = "1 2 2"
        self.assertEqual(iq_test(s), 1)

        s = "88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46"
        self.assertEqual(iq_test(s), 4)

        s = "100 99 100"
        self.assertEqual(iq_test(s), 2)

        s = "5 3 2"
        self.assertEqual(iq_test(s), 3)

        s = "43 28 1 91"
        self.assertEqual(iq_test(s), 2)

        s = "20 94 56 50 10 98 52 32 14 22 24 60 4 8 98 46 34 68 82 82 98 90 \
             50 20 78 49 52 94 64 36"
        self.assertEqual(iq_test(s), 26)

        s = "79 27 77 57 37 45 27 49 65 33 57 21 71 19 75 85 65 61 23 97 85 9 \
             23 1 9 3 99 77 77 21 79 69 15 37 15 7 93 81 13 89 91 31 45 93 15 \
             97 55 80 85 83"
        self.assertEqual(iq_test(s), 48)

        s = "100 100 1"
        self.assertEqual(iq_test(s), 3)

        s = "9 31 27 93 17 77 75 9 9 53 89 39 51 99 5 1 11 39 27 49 91 17 27 \
             79 81 71 37 75 35 13 93 4 99 55 85 11 23 57 5 43 5 61 15 35 23 \
             91 3 81 99 85 43 37 39 27 5 67 7 33 75 59 13 71 51 27 15 93 51 \
             63 91 53 43 99 25 47 17 71 81 15 53 31 59 83 41 23 73 25 91 9"
        self.assertEqual(iq_test(s), 32)


if __name__ == '__main__':
    unittest.main()

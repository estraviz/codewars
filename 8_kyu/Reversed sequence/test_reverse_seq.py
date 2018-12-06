import unittest
from reverse_seq import reverse_seq


class Testreverse_seq(unittest.TestCase):

    def test_reverse_seq(self):
        self.assertEqual(reverse_seq(5), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_seq(6), [6, 5, 4, 3, 2, 1])
        self.assertEqual(reverse_seq(100), list(range(1, 101))[::-1])
        self.assertEqual(reverse_seq(10000), list(range(1, 10001))[::-1])
        self.assertEqual(reverse_seq(100000), list(range(1, 100001))[::-1])
        self.assertEqual(reverse_seq(1000000), list(range(1, 1000001))[::-1])


if __name__ == '__main__':
    unittest.main()

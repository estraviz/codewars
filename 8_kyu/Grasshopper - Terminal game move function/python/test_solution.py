import unittest

from solution import move


class TestSolution(unittest.TestCase):

    def test_cases_basic(self):
        self.assertEqual(move(0, 4), 8)
        self.assertEqual(move(3, 6), 15)
        self.assertEqual(move(2, 5), 12)

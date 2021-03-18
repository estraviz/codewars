import unittest

from solution import mutate


ZERO = '0' * 100
ONE = '1' * 100


class TestClass(unittest.TestCase):

    def test_100_pct_mutate(self):
        assert mutate(ZERO, 1) == ONE
        assert mutate(ONE, 1) == ZERO

    def test_0_pct_mutate(self):
        assert mutate(ZERO, 0) == ZERO
        assert mutate(ONE, 0) == ONE

    def test_50_pct_mutate(self):
        assert '0' in mutate(ZERO, 0.5)
        assert '1' in mutate(ONE, 0.5)


if __name__ == "__main__":
    unittest.main()

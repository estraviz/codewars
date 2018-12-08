import unittest
from am_i_wilson import am_i_wilson


class TestAmIWilson(unittest.TestCase):

    def test_am_i_wilson(self):
        self.assertFalse(am_i_wilson(0))
        self.assertFalse(am_i_wilson(1))
        self.assertTrue(am_i_wilson(5))
        self.assertFalse(am_i_wilson(8))
        self.assertFalse(am_i_wilson(9))
        self.assertFalse(am_i_wilson(11))
        self.assertTrue(am_i_wilson(13))
        self.assertFalse(am_i_wilson(101))
        self.assertTrue(am_i_wilson(563))
        self.assertFalse(am_i_wilson(569))


if __name__ == '__main__':
    unittest.main()

import unittest
from authenticate import Sleigh


class TestSleigh(unittest.TestCase):
    def setUp(self):
        self.sleigh = Sleigh()

    def test_correct_credentials(self):
        self.assertTrue(self.sleigh.authenticate('Santa Claus', 'Ho Ho Ho!'))

    def test_incorrect_credentials(self):
        self.assertFalse(self.sleigh.authenticate('Santa', 'Ho Ho Ho!'))
        self.assertFalse(self.sleigh.authenticate('Santa Claus', 'Ho Ho Ho'))
        self.assertFalse(self.sleigh.authenticate('Santa Claus', 'Ho Ho!'))
        self.assertFalse(self.sleigh.authenticate('Easter Bunny', 'Ho Ho Ho!'))
        self.assertFalse(self.sleigh.authenticate('jhoffner', 'CodeWars'))


if __name__ == '__main__':
    unittest.main()

import unittest
from find_missing_letter import find_missing_letter


class TestFindMissingLetter(unittest.TestCase):

    def test_going_to_zero_or_to_infinity(self):
        self.assertEqual(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')
        self.assertEqual(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')
        self.assertEqual(find_missing_letter(['b', 'd']), 'c')


if __name__ == '__main__':
    unittest.main()

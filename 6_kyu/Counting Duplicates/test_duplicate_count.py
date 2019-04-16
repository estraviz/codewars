import unittest
from duplicate_count import duplicate_count


class TextFindEvenIndex(unittest.TestCase):

    def test_duplicate_count(self):
        self.assertEqual(duplicate_count(""), 0)
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdeaa"), 1)
        self.assertEqual(duplicate_count("abcdeaB"), 2)
        self.assertEqual(duplicate_count("Indivisibilities"), 2)

        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self.assertEqual(duplicate_count(lowercase), 0)
        self.assertEqual(duplicate_count(lowercase + "aaAb"), 2)

        self.assertEqual(duplicate_count(lowercase + lowercase), 26)
        self.assertEqual(duplicate_count(lowercase + uppercase), 26)


if __name__ == '__main__':
    unittest.main()

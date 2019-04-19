import unittest
from average_string import average_string


class TextAverageString(unittest.TestCase):

    def test_average_string(self):
        self.assertEqual(average_string("zero nine five two"), "four")
        self.assertEqual(average_string("four six two three"), "three")
        self.assertEqual(average_string("one two three four five"), "three")
        self.assertEqual(average_string("five four"), "four")
        self.assertEqual(average_string("zero zero zero zero zero"), "zero")
        self.assertEqual(average_string("one one eight one"), "two")
        self.assertEqual(average_string("one"), "one")
        self.assertEqual(average_string(""), "n/a")
        self.assertEqual(average_string("ten"), "n/a")
        self.assertEqual(average_string("pippi"), "n/a")


if __name__ == '__main__':
    unittest.main()

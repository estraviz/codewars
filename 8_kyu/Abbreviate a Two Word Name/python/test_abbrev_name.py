import unittest
from abbrev_name import abbrev_name


class TestAbbrevName(unittest.TestCase):

    def test_abbrev_name(self):
        self.assertEqual(abbrev_name("Sam Harris"), "S.H")
        self.assertEqual(abbrev_name("Patrick Feenan"), "P.F")
        self.assertEqual(abbrev_name("Evan Cole"), "E.C")
        self.assertEqual(abbrev_name("P Favuzzi"), "P.F")
        self.assertEqual(abbrev_name("David Mendieta"), "D.M")


if __name__ == "__main__":
    unittest.TestCase()

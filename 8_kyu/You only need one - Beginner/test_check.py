import unittest
from check import check


class TestBasicOp(unittest.TestCase):

    def test_check(self):
        self.assertTrue(check((66, 101), 66))

        self.assertFalse(check((78, 117, 110, 99, 104, 117, 107, 115), 8))

        self.assertTrue(check((101, 45, 75, 105, 99, 107), 107))

        self.assertTrue(check((80, 117, 115, 104, 45, 85, 112, 115), 45))

        self.assertTrue(check(('t', 'e', 's', 't'), 'e'))

        self.assertFalse(check(("what", "a", "great", "kata"), "kat"))

        self.assertTrue(check((66, "codewars", 11, "alex loves pushups"),
                        "alex loves pushups"))

        self.assertFalse(check(("come", "on", 110, "2500", 10, '!', 7, 15),
                               "Come"))

        self.assertTrue(check(("when's", "the", "next", "Katathon?", 9, 7),
                        "Katathon?"))

        self.assertFalse(check((8, 7, 5, "bored", "of", "writing", "tests",
                                115), 45))

        self.assertTrue(check(("anyone", "want", "to", "hire", "me?"), "me?"))


if __name__ == '__main__':
    unittest.main()

import unittest
from smash import smash


class TestSmash(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(smash([]), "")

    def test_none(self):
        self.assertRaises(TypeError, smash, None)

    def test_one_word(self):
        self.assertEqual(smash(["hello"]), "hello")

    def test_multiple_words(self):
        input_lst = ["hello", "world"]
        self.assertEqual(smash(input_lst), "hello world")

        input_lst = ["hello", "amazing", "world"]
        self.assertEqual(smash(input_lst), "hello amazing world")

        input_lst = ["this", "is", "a", "really", "long", "sentence"]
        self.assertEqual(smash(input_lst), "this is a really long sentence")


if __name__ == '__main__':
    unittest.main()

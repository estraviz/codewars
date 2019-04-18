import unittest
from namelist import namelist


class TextNameList(unittest.TestCase):

    def test_many_names(self):
        names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'},
                 {'name': 'Homer'}, {'name': 'Marge'}]
        self.assertEqual(namelist(names), 'Bart, Lisa, Maggie, Homer & Marge')

        names = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
        self.assertEqual(namelist(names), 'Bart, Lisa & Maggie')

    def test_two_names(self):
        names = [{'name': 'Bart'}, {'name': 'Lisa'}]
        self.assertEqual(namelist(names), 'Bart & Lisa')

    def test_one_name(self):
        names = [{'name': 'Bart'}]
        self.assertEqual(namelist(names), 'Bart')

    def test_no_names(self):
        names = []
        self.assertEqual(namelist(names), '')


if __name__ == '__main__':
    unittest.main()

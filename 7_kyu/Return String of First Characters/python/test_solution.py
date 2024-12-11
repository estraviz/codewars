import unittest

from solution import make_string


class TestSolution(unittest.TestCase):

    def test_basic_tests(self):
        self.assertEqual(make_string("sees eyes xray yoat"), "sexy", "Wrong result for 'sees eyes xray yoat'")
        self.assertEqual(make_string("brown eyes are nice"), "bean", "Wrong result for 'brown eyes are nice'")
        self.assertEqual(make_string("cars are very nice"), "cavn", "Wrong result for 'cars are very nice'")
        self.assertEqual(make_string("kaks de gan has a big head"), "kdghabh", "Wrong result for 'kaks de gan has a big head'")

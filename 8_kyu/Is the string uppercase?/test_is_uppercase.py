import unittest
from is_uppercase import is_uppercase


class TestIsUpperCase(unittest.TestCase):

    def test_is_uppercase(self):
        self.assertFalse(is_uppercase("c"))
        self.assertTrue(is_uppercase("C"))
        self.assertFalse(is_uppercase("hello I AM DONALD"))
        self.assertTrue(is_uppercase("HELLO I AM DONALD"))
        self.assertFalse(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ"))
        self.assertTrue(is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"))

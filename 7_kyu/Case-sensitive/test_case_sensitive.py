from case_sensitive import case_sensitive
from Test import Test
import unittest

# Using built-in Test.py class: $ python test_case_sensitive
test = Test()

test.describe("Basic Tests")
test.it("Sample Tests")
test.assert_equals(case_sensitive('asd'), [True, []])
test.assert_equals(case_sensitive('cellS'), [False, ['S']])
test.assert_equals(case_sensitive('z'), [True, []])
test.assert_equals(case_sensitive(''), [True, []])


# Using pytest: $ pytest -v test_case_sensitive
def test_basic_tests():
    assert case_sensitive('asd') == [True, []]
    assert case_sensitive('cellS') == [False, ['S']]
    assert case_sensitive('z') == [True, []]
    assert case_sensitive('') == [True, []]


# Using unittest: $ python -m unittest -v test_case_sensitive.Testing
class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()

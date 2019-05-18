import unittest
from valid_parentheses import valid_parentheses


class TestValidParentheses(unittest.TestCase):

    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses(")"), False)
        self.assertEqual(valid_parentheses("("), False)
        self.assertEqual(valid_parentheses(""), True)
        self.assertEqual(valid_parentheses("hi)("), False)
        self.assertEqual(valid_parentheses("hi(hi)"), True)
        self.assertEqual(valid_parentheses("("), False)
        self.assertEqual(valid_parentheses("hi(hi)("), False)
        self.assertEqual(valid_parentheses("((())()())"), True)
        self.assertEqual(valid_parentheses("(c(b(a)))(d)"), True)
        self.assertEqual(valid_parentheses("hi(hi))("), False)


if __name__ == '__main__':
    unittest.main()

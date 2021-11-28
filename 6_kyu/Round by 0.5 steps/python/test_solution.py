import unittest

import codewars_test as test

from solution import solution


class TestStringMethods(unittest.TestCase):

    def test_solution(self):
        test.assert_equals(solution(4.2), 4)
        test.assert_equals(solution(4.25), 4.5)
        test.assert_equals(solution(4.4), 4.5)
        test.assert_equals(solution(4.6), 4.5)
        test.assert_equals(solution(4.75), 5)
        test.assert_equals(solution(4.8), 5)
        test.assert_equals(solution(4.5), 4.5)
        test.assert_equals(solution(4.55), 4.5)
        test.assert_equals(solution(4.74), 4.5)
        test.assert_equals(solution(4.74999999999), 4.5)
        test.assert_equals(solution(4.7499999999+.00000000001), 4.5)
        test.assert_equals(solution(4.7499999999+.0000000001), 5)


if __name__ == '__main__':
    unittest.main()


# Note:
#   install CW's testing framework like this:
#       $ python -m pip install git+https://github.com/codewars/python-test-framework.git@ba881f9221f9086e97ec6f7baf43722bc5fbbe5b
#   where the hash after ...git@ points to the commit for release 0.2.0 (the latest one as of Nov 29, 2021)
#   Run test like this:
#       $ python -m unittest
#   (BTW I still prefer pytest for almost everything ;-)

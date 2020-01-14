"""
Simple rotated palindromes
"""


def solve(st):
    for _ in st:
        st = st[-1] + st[:-1]
        if is_palindrome(st):
            return True
    return False


def is_palindrome(s):
    return s == s[::-1]

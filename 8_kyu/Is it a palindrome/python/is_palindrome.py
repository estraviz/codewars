"""
Is it a palindrome?
"""


def is_palindrome(s):
    return s.lower() == s[::-1].lower()

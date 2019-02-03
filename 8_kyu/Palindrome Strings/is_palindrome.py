"""Palindrome Strings
"""


def is_palindrome(string):
    return str(string) == str(string)[::-1]

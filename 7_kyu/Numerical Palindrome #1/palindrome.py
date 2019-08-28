"""
Numerical Palindrome #1
"""


def palindrome(num):
    return "Not valid" if type(num) != int or num < 0 else num == int(
        str(num)[::-1])

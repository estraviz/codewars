"""
Numerical Palindrome #1.5
"""


def palindrome(num, s):
    return get_palindromes(num,
                           s) if is_valid(num) and is_valid(s) else "Not valid"


def get_palindromes(n, s):
    lst = []
    while len(lst) < s:
        if n > 9 and is_palindrome(n):
            lst.append(n)
        n += 1
    return lst


def is_palindrome(n):
    return n == int(str(n)[::-1])


def is_valid(x):
    return type(x) == int and x >= 0

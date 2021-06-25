"""Next Palindromic Number."""


def next_pal(val):
    next = val + 1
    while not is_palindrome(next):
        next += 1
    return next


def is_palindrome(n):
    return str(n) == str(n)[::-1]

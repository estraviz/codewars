"""Factorial"""


def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    else:
        if n in {0, 1}:
            return 1
        else:
            return n * factorial(n - 1)

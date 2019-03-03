"""You're a square!
"""
from math import sqrt


def is_square(n):
    return n == sum(2*k - 1 for k in range(1, int(sqrt(n)) + 1)) \
        if n >= 0 else False

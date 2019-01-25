"""To square(root) or not to square(root)
"""
from math import sqrt


def square_or_square_root(arr):
    return list(map(lambda num: sqrt(num)
                    if has_integer_sqrt(num) else num**2, arr))


def has_integer_sqrt(num):
    return int(sqrt(num)) == sqrt(num)

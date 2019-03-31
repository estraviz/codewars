"""Persistent Bugger
"""
from functools import reduce


def persistence(n):
    if n < 10:
        return 0
    return 1 + persistence(reduce(lambda x, y: x*y, [int(n) for n in str(n)]))

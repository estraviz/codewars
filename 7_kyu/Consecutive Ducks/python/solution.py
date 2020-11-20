"""Consecutive Ducks
"""

from math import log


def consecutive_ducks(n):
    # Any number can be expressed as a sum of consecutive numbers provided that
    # n != 2^k (k € N)
    return False if int(log(n, 2)) == log(n, 2) else True

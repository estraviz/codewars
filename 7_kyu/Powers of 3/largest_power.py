"""
Powers of 3
"""

from math import floor, log


def largest_power(N):
    k = floor(log(N) / log(3))
    return k if 3**k < N else k - 1

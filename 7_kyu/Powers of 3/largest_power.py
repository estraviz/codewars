"""
Powers of 3
"""

from math import log


def largest_power(N):
    k = int(log(N, 3))
    return k if 3**k < N else k - 1

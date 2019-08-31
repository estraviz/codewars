"""
Power of two
"""

from math import log


def power_of_two(x):
    try:
        exp = int(log(x, 2))
    except ValueError:
        return False
    else:
        return True if 2**exp == x else False

"""
Number of Divisions
"""

from math import log


def divisions(n, divisor):
    return int(log(n, divisor))

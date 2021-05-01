"""Speed Control"""

from math import floor


def gps(s, x):
    return 0 if len(x) <= 1 else floor(3600 * max([d2 - d1 for d1, d2 in zip(x[:-1], x[1:])])/s)

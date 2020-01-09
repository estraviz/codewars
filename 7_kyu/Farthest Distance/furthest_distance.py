"""
Farthest Distance
"""

from itertools import combinations
from math import sqrt


def furthest_distance(arr):
    return round(max(dist(x, y) for [x, y] in list(combinations(arr, 2))), 2)


def dist(p, q):
    return sqrt(sum((pi - qi)**2.0 for pi, qi in zip(p, q)))

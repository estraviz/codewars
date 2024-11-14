"""
Difference of Volumes of Cuboids
"""

from functools import reduce


def find_difference(a, b):
    return abs(get_volume(a) - get_volume(b))


def get_volume(lst):
    return reduce(lambda x, y: x * y, lst)

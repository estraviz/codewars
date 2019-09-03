"""
Array Mash
"""

from itertools import chain


def array_mash(a, b):
    return list(chain(*zip(a, b)))

"""
Array Mash
"""

from itertools import chain


def array_mash(a, b):
    return list(chain.from_iterable([item for item in zip(a, b)]))

"""
Flatten and sort an array
"""

from itertools import chain


def flatten_and_sort(array):
    return sorted(chain(*array))

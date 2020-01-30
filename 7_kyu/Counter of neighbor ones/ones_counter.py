"""
Counter of neighbor ones
"""

from itertools import groupby


def ones_counter(input):
    return [sum(group) for key, group in groupby(input) if key]

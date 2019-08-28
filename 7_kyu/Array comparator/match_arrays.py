"""
Array comparator
"""


def match_arrays(v, r):
    return sum(1 for elem in v if elem in r)

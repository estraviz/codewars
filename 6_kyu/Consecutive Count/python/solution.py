"""Consecutive Count"""

from itertools import groupby


def get_consecutive_items(items, key):
    cons = [
        ((int(chr) if type(items) == int else chr), sum(1 for _ in group))
        for chr, group in groupby(str(items))
    ]
    try:
        return max(filter(lambda x: x[0] == key, cons), key=lambda y: y[1])[1]
    except ValueError:
        return 0

"""Unique In Order
"""
from itertools import groupby


def unique_in_order(iterable):
    return [key for key, group in groupby(iterable)]

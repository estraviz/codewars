"""Stones on the Table
"""

from itertools import groupby


def solution(stones):
    grouped = [list(g) for k, g in groupby(stones)]
    return sum(len(elems) - 1 for elems in grouped)

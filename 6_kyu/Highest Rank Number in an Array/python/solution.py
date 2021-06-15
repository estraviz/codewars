"""Highest Rank Number in an Array"""

from collections import Counter


def highest_rank(arr):
    return sorted([(val, key) for key, val in sorted(Counter(arr).items(), reverse=True)], reverse=True)[0][1]

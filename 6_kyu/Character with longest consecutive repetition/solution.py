"""Character with longest consecutive repetition
"""

from itertools import groupby


def longest_repetition(chars):
    results = [(chr, sum(1 for _ in group)) for chr, group in groupby(chars)]
    return max(results, key=lambda item: item[1]) if results else ("", 0)

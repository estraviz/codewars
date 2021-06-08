"""Ordered Count of Characters"""

from collections import Counter


def ordered_count(inp):
    return list(Counter(inp).items())

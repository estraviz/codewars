"""
Sum it continuously
"""

from itertools import accumulate


def add(l):
    return [*accumulate(l)] if isinstance(l, list) and all(
        isinstance(num, int) for num in l) else 'Invalid input'

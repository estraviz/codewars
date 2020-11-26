"""
Consecutive letters
"""

from string import ascii_lowercase as lc


def solve(st):
    ordered = sorted(list(st))
    return (lc.index(ordered[-1]) - lc.index(ordered[0]) + 1) == len(st)

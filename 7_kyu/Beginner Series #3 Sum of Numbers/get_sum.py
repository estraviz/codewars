"""Beginner Series #3 Sum of Numbers
"""


def get_sum(a, b):
    return sum(x for x in range(min(a, b), max(a, b) + 1))

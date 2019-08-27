"""
Return the first M multiples of N
"""


def multiples(m, n):
    return [k * n for k in range(1, m + 1)]

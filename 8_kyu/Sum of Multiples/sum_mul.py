"""
Sum of Multiples
"""


def sum_mul(n, m):
    return 'INVALID' if m <= 0 or n <= 0 else sum(range(n, m, n))

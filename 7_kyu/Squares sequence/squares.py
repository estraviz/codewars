"""
Squares sequence
"""


def squares(x, n):
    return [] if n <= 0 else [x] + [x**(2**k) for k in range(1, n)]

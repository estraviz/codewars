"""
Squares sequence
"""


def squares(x, n):
    return [x**(2**k) for k in range(n)]

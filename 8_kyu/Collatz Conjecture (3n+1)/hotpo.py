"""Collatz Conjecture (3n+1)
"""


def hotpo(n):
    if n == 1:
        return 0
    return 1 + hotpo(n/2 if n % 2 == 0 else 3*n + 1)

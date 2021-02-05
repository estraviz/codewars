"""Memoized Fibonacci"""

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

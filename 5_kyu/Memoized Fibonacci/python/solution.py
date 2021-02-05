"""Memoized Fibonacci"""

memo = {}


def fibonacci(n):
    if n in memo:
        return memo[n]
    if n in [1, 2]:
        memo[n] = 1
        return 1
    elif n > 2:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

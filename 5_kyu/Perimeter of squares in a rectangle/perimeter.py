"""
Perimeter of squares in a rectangle
"""


def perimeter(n):
    return 4 * sum(fib(n))


def fib(n):
    a, b = 1, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b

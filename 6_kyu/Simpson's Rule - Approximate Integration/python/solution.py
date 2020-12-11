"""Simpson's Rule - Approximate Integration"""

from math import pi, sin


def simpson(n):
    a, b = 0, pi
    h = (b - a) / n
    factor = (b - a) / (3 * n)
    sum1 = 4 * sum(fun(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1))
    sum2 = 2 * sum(fun(a + 2 * i * h) for i in range(1, n // 2))
    return factor * (fun(a) + fun(b) + sum1 + sum2)


def fun(x):
    return (3 / 2) * (sin(x)) ** 3

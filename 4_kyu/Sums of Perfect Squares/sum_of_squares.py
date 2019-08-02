"""
Sums of Perfect Squares
"""

from math import sqrt


def sum_of_squares(n):
    """
    Lagrange's four-square theorem, also known as Bachet's conjecture,
    states that every natural number can be represented as the sum of
    four integer squares.

    n = a**2 + b**2 + c**2 + d**2

    where the four numbers a, b, c, d are integers.

    Ref.: https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
    Ref.: http://mathworld.wolfram.com/LagrangesFour-SquareTheorem.html
    """
    while n & 3 == 0:
        n = n >> 2
    if n % 8 == 7:
        return 4
    if is_square(n):
        return 1
    for i in range(1, int(sqrt(n)) + 1):
        if is_square(n - i**2):
            return 2
    return 3


def is_square(n):
    return n == int(sqrt(n))**2

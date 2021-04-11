"""Difference Of Squares"""


def difference_of_squares(n):
    return sum(range(1, n+1))**2 - sum(x**2 for x in range(1, n+1))

"""
Count the Digit
"""


def nb_dig(n, d):
    squares = (k**2 for k in range(0, n+1))
    return sum(str(sq).count(str(d)) for sq in squares)

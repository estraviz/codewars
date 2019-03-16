"""Find the next perfect square!
"""
from math import sqrt


def find_next_square(sq):
    num = int(sqrt(sq))
    return (num + 1)**2 if num**2 == sq else -1

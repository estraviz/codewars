"""Multiplicative Persistence... What's special about 277777788888899?"""

from functools import reduce
from operator import mul


def per(n):
    lst = []
    while not is_single_digit(n):
        lst.append(n := reduce(mul, map(int, str(n))))
    return lst


def is_single_digit(n):
    return n <= 9

"""Multiplicative Persistence... What's special about 277777788888899?"""

from functools import reduce


def per(n):
    lst = []
    while is_not_single_digit(n):
        lst.append(n := get_reduced_next(n))
    return lst


def is_not_single_digit(n):
    return n >= 10


def get_reduced_next(n):
    return reduce((lambda x, y: x * y), get_list_of_digits(n))


def get_list_of_digits(n):
    return list(int(x) for x in list(str(n)))

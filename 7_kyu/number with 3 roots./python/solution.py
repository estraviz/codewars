"""number with 3 roots."""


from math import sqrt


def perfect_roots(n):
    return sqrt(sqrt(sqrt(n))).is_integer()

"""Gauß needs help! (Sums of a lot of numbers)."""


def f(n):
    return n * (1 + n) / 2 if type(n) == int and n > 0 else None

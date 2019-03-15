"""Descending Order
"""


def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

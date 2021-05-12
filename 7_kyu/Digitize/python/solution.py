"""Digitize"""


def digitize(n):
    return [int(x) for x in str(n) if x.isdigit()]

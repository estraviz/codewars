"""Unlimited Sum"""


def sum(*args):
    _sum = 0
    for x in args:
        if isinstance(x, int):
            _sum += x
    return _sum

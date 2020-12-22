"""Unique string characters"""


def solve(a, b):
    return get_uncommon(a, b) + get_uncommon(b, a)


def get_uncommon(a, b):
    return "".join(c for c in a if c not in b)

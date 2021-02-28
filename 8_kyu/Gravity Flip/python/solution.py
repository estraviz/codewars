"""Gravity Flip"""


def flip(d, a):
    return sorted(a, reverse=True if d == 'L' else False)

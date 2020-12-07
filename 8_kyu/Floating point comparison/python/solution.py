"""Floating point comparison"""


def approx_equals(a, b):
    return abs(a - b) < 0.001

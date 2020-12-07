"""Floating point comparison"""

from math import isclose


def approx_equals(a, b):
    return isclose(a, b, abs_tol=1e-3)

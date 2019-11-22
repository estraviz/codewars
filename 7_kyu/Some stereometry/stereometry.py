"""
Some stereometry
"""

from math import sqrt, pi


def stereometry(r, h):
    r_circle = sqrt(r**2 - h**2)
    return round(4 * pi * r**2, 3), round(pi * r_circle**2,
                                          3), round(2 * pi * r_circle, 3)

"""Volumne of a cup
"""
from math import pi as PI


def cup_volume(d1, d2, height):
    r1, r2 = d1/2., d2/2.
    return round(height*PI*(r1**2 + r2**2 + r1*r2)/3, 2)

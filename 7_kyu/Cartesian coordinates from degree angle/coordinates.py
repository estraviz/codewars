"""
Cartesian coordinates from degree angle
"""

from math import cos, sin, pi


def coordinates(degrees, radius):
    x = radius*cos(degrees*pi/180)
    y = radius*sin(degrees*pi/180)
    return tuple(round(cartesian, 10) for cartesian in (x, y))

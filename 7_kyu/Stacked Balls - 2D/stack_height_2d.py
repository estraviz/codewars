"""
Stacked Balls - 2D
"""

from math import pi, sin


def stack_height_2d(layers):
    return layers if layers <= 1 else round(1 + (layers - 1) * sin(pi / 3), 3)

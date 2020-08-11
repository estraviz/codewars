"""Area of an annulus
"""

from math import pi as PI
from math import sin, tan


def annulus_area(a):
    # sin PI/3 = (r + R) / a -> R = a*sin(PI/3) - r
    # tan PI/6 = (R - r) / (a/2) -> r = R - (a/2)*tan(PI/6)
    # -> r = (1/2)*(a*sin(PI/3) - (a/2)*tan(PI/6))
    r = (1/2)*(a*sin(PI/3) - (a/2)*tan(PI/6))
    R = a*sin(PI/3) - r
    return round(PI*(R**2 - r**2), 2)

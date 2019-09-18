"""
Square Pi's
"""

from math import sqrt, ceil


def square_pi(digits):
    pi_digits = '314159265358979323846264338327950288419716939937510' \
                '58209749445923078164062862089986280348253421170679'
    return ceil(sqrt(sum(map(lambda x: int(x)**2, pi_digits[0:digits]))))

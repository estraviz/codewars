"""
SpeedCode #2 - Array Madness
"""


def array_madness(a, b):
    return sum(a_i**2 for a_i in a) > sum(b_i**3 for b_i in b)

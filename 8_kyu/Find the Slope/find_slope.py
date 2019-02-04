"""Find the Slope
"""


def find_slope(points):
    a, b, c, d = points
    try:
        return str((d - b) // (c - a))
    except ZeroDivisionError:
        return 'undefined'

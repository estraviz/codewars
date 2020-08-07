"""
Invert The Triangle
"""


def invert_triangle(t):
    lst = [{" ": "#", "#": " "}.get(c, c) for c in t]
    return ''.join(x for x in lst[::-1])

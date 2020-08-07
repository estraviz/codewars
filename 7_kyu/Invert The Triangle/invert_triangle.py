"""
Invert The Triangle
"""


def invert_triangle(t):
    return t.translate(str.maketrans({"#": " ", " ": "#"}))[::-1]

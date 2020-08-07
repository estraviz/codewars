"""
Invert The Triangle
"""


def invert_triangle(t):
    lst = []
    for c in t:
        if c == " ":
            lst.append("#")
        elif c == "#":
            lst.append(" ")
        else:
            lst.append(c)
    return ''.join(x for x in lst[::-1])

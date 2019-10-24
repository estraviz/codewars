"""
Squares sequence
"""


def squares(x, n):
    arr = []
    if n > 0:
        arr.append(x)
        for _ in range(n - 1):
            x = x**2
            arr.append(x)
    return arr

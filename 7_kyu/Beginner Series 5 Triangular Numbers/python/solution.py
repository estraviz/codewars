"""Beginner Series #5 Triangular Numbers"""


def is_triangular(t):
    t = int(t)
    for x in range(t+1):
        if check_triangular(t, x):
            return True
    return False


def check_triangular(t, x):
    return t == int(x * (x + 1) / 2)

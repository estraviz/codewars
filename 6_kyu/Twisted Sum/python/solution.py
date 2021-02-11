"""Twisted Sum"""


def compute_sum(n):
    return sum(int(y) for y in list("".join(str(x) for x in range(1, n + 1))))

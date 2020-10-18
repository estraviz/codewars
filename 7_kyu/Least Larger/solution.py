"""Least Larger
"""


def least_larger(a, i):
    try:
        return a.index(min(x for x in a if x > a[i]))
    except ValueError:
        return -1

"""Difference between two collections"""


def diff(a, b):
    return sorted(set(a) ^ set(b))

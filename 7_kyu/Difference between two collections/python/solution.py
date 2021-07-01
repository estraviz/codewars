"""Difference between two collections"""


def diff(a, b):
    return sorted(set(not_in(a, b) + not_in(b, a)))


def not_in(a, b):
    return [x for x in a if x not in b]

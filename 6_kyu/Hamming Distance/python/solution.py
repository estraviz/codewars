"""Hamming Distance"""


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

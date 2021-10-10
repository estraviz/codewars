"""Hamming Distance"""


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

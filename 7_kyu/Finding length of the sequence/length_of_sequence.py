"""
Finding length of the sequence
"""


def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    else:
        gen = (i for i, c in enumerate(arr) if c == n)
        first = next(gen)
        return next(gen) - first + 1

"""Simple consecutive pairs
"""


def pairs(arr):
    tuples = zip(*[arr[i::2] for i in range(2)])
    return sum(1 for (x, y) in tuples if is_consecutive(x, y))


def is_consecutive(x, y):
    return x + 1 == y or x == y + 1

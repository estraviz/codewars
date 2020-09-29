"""Simple consecutive pairs
"""


def pairs(arr):
    tuples = zip(*[arr[i::2] for i in range(2)])
    return sum(1 for (x, y) in tuples if max(x, y) - min(x, y) == 1)

"""Simple consecutive pairs
"""


def pairs(arr):
    return sum(max(x, y) - min(x, y) == 1 for x, y in zip(arr[::2], arr[1::2]))

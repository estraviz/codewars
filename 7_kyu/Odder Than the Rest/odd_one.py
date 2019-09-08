"""
Odder Than the Rest
"""


def odd_one(arr):
    for x in arr:
        if x % 2 != 0:
            return arr.index(x)
    return -1

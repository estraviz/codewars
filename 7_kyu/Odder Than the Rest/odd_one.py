"""
Odder Than the Rest
"""


def odd_one(arr):
    try:
        return [arr.index(x) for x in arr if x % 2 != 0].pop()
    except IndexError:
        return -1

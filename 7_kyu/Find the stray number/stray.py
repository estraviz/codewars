"""
Find the stray number
"""


def stray(arr):
    return min(arr, key=lambda x: arr.count(x))

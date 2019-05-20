"""Find the unique number
"""


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

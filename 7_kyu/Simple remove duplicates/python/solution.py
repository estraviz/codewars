"""Simple remove duplicates"""


def solve(arr):
    return [x for i, x in enumerate(arr) if x not in arr[i + 1 :]]

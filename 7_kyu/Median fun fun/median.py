"""
Median fun fun
"""


def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 1:
        mid = (len(arr) - 1) // 2
        return arr[mid]
    else:
        mid1 = len(arr) // 2 - 1
        mid2 = len(arr) // 2
        return (arr[mid1] + arr[mid2]) / 2

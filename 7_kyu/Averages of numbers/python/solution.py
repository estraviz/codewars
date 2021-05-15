"""Averages of numbers"""


def averages(arr):
    return [] if (not arr or len(arr) == 1) else [(x+y)/2 for x, y in zip(arr, arr[1:])]

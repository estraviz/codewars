"""
Find all pairs
"""


def duplicates(arr):
    return sum(arr.count(num) // 2 for num in set(arr))

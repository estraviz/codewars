"""
Merging sorted integer arrays (without duplicates)
"""


def merge_arrays(first, second):
    return sorted(set(first + second))

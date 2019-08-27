"""
Flatten and sort an array
"""


def flatten_and_sort(array):
    return sorted([elem for lst in array for elem in lst])

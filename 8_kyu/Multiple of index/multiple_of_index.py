"""
Multiple of index
"""


def multiple_of_index(arr):
    return [elem for i, elem in enumerate(arr) if i != 0 and elem % i == 0]

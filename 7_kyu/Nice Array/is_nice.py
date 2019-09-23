"""
Nice Array
"""


def is_nice(arr):
    if not arr:
        return False
    for elem in arr:
        if elem - 1 not in arr and elem + 1 not in arr:
            return False
    return True

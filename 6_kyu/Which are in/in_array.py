"""Which are in?
"""


def in_array(array1, array2):
    return sorted(set(a1 for a1 in array1 for a2 in array2 if a1 in a2))

"""
CSV representation of array
"""


def toCsvText(array) :
    return '\n'.join(','.join(str(c) for c in arr) for arr in array)

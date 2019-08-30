"""
Form The Minimum
"""


def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))

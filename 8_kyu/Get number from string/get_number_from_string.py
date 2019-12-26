"""
Get number from string
"""

from string import digits


def get_number_from_string(string):
    return int(''.join(ch for ch in string if ch in digits))

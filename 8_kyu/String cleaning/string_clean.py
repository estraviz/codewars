"""String cleaning
"""
from string import digits


def string_clean(s):
    """
    Function will return the cleaned string
    """
    return s.translate(s.maketrans('', '', digits))

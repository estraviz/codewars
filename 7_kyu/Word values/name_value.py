"""
Word values
"""

from string import ascii_letters as letters


def name_value(my_list):
    return [
        (i + 1) *
        sum(letters.index(ltr) + 1 if ltr in letters else 0 for ltr in str_)
        for i, str_ in enumerate(my_list)
    ]

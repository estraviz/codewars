"""Disemvowel Trolls
"""


def disemvowel(string):
    table = str.maketrans(dict.fromkeys('aeiouAEIOU'))
    return string.translate(table)

"""Correct the mistakes of the character recognition software
"""


def correct(string):
    return string.translate(str.maketrans({'5': 'S', '0': 'O', '1': 'I'}))

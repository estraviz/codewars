"""
Coding 3min: Father and Son
"""


def sc(s):
    return ''.join(letter for letter in s if letter.swapcase() in s)

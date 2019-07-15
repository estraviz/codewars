"""
Find the position?
"""

from string import ascii_lowercase


def position(alphabet):
    return f'Position of alphabet: {ascii_lowercase.index(alphabet.lower())+1}'

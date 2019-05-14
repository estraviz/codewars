"""Replace With Alphabet Position
"""
from string import ascii_letters


def alphabet_position(text):
    return " ".join(str(ascii_letters.index(x.lower()) + 1) for x in text
                    if x.isalpha())

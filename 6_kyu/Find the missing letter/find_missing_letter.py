"""Find the missing letter
"""
from string import ascii_letters


def find_missing_letter(chars):
    idx = ascii_letters.index(chars[0])
    for i, letter in enumerate(chars):
        if i + idx != ascii_letters.index(letter):
            return ascii_letters[i + idx]

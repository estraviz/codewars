"""Simple Pig Latin
"""
from string import ascii_letters


def pig_it(text):
    return " ".join(["".join([word[1:],
                              word[0],
                              'ay' if word[0] in ascii_letters else ''])
                     for word in text.split()])

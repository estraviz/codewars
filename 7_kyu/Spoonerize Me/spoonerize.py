"""Spoonerize Me
"""


def spoonerize(words):
    word1, word2 = words.split()
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

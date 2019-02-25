"""Shortest Word
"""


def find_short(s):
    return min(len(word) for word in s.split(' '))

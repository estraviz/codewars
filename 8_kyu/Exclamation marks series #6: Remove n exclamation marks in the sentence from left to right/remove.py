"""
Exclamation marks series #6:
    Remove n exclamation marks in the sentence from left to right
"""


def remove(s, n):
    return s.replace('!', '', n)

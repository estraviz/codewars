"""Exclamation marks series #1 Remove a exclamation mark from the end of string
"""


def remove(s):
    return s[:-1] if s.endswith('!') else s

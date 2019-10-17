"""
Alphabetically ordered
"""


def alphabetic(s):
    if len(s) < 2:
        return True
    for i, j in zip(s[:-1], s[1:]):
        if ord(i) > ord(j):
            return False
    return True

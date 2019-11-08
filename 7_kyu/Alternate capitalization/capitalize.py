"""
Alternate capitalization
"""


def capitalize(s):
    word = ''.join(c.upper() if i % 2 == 0 else c for i, c in enumerate(s))
    return [word, word.swapcase()]

"""
Reverse every other word in the string
"""


def reverse_alternate(string):
    return ' '.join([
        word[::-1] if i % 2 != 0 else word
        for i, word in enumerate(string.split())
    ])

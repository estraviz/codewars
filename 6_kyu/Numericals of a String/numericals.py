"""
Numericals of a String
"""


def numericals(s):
    chars = {}
    result = ""
    for c in s:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
        result += str(chars[c])
    return result

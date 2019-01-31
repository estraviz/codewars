"""Squash the bugs
"""


def find_longest(string):
    spl = string.split()
    longest = 0
    i = 0
    while (i < len(spl)):
        if len(spl[i]) > longest:
            longest = len(spl[i])
        i += 1
    return longest

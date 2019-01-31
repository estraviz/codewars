"""Squash the bugs
"""


def find_longest(string):
    return max(list(map(lambda x: len(x), string.split(" "))))

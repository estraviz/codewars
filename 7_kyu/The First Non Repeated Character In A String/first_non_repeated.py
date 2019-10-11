"""
The First Non Repeated Character In A String
"""


def first_non_repeated(s):
    for c in s:
        if s.count(c) == 1:
            return c

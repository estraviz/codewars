"""
The First Non Repeated Character In A String
"""


def first_non_repeated(s):
    times = {}
    for c in s:
        if c in times:
            times[c] += 1
        else:
            times[c] = 1
    for c in s:
        if times[c] == 1:
            return c

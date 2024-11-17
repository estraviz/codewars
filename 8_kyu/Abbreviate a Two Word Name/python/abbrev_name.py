"""Abbreviate a Two Word Name
"""


def abbrev_name(name):
    first, last = name.upper().split()
    return f'{first[0]}.{last[0]}'

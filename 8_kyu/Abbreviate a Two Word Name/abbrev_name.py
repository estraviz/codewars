"""Abbreviate a Two Word Name
"""


def abbrev_name(name):
    name_list = name.upper().split()
    return f'{name_list[0][0]}.{name_list[1][0]}'

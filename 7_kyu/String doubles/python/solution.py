"""
String doubles
"""

from itertools import groupby


def doubles(s, prev=""):
    new_s = "".join([k for k, g in groupby(s) if len(list(g)) % 2 != 0])
    if prev == "":
        return doubles(new_s, new_s)
    else:
        if s == new_s:
            return new_s
        else:
            return doubles(new_s, s)

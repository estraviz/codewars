# Valid Spacing
from itertools import groupby


def valid_spacing(s):
    if s:
        if s[0] == ' ' or s[-1] == ' ':
            return False
        for _, g in groupby(s, key=None):
            group = list(g)
            if group[0] == ' ' and len(group) > 1:
                return False
    return True

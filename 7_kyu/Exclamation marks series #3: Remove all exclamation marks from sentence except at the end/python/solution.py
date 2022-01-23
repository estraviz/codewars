# Exclamation marks series #3: Remove all exclamation marks from sentence except at the end
from collections import Counter


def remove(s):
    num_excl_tot = Counter(s)['!']
    num_excl_end = 0
    for c in s[::-1]:
        if c == '!':
            num_excl_end += 1
        else:
            break
    return s.replace('!', '', num_excl_tot-num_excl_end)

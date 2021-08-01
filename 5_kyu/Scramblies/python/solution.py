"""Scramblies"""

from collections import Counter


def scramble(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    for k2, v2 in c2.items():
        if k2 not in c1.keys() or v2 > c1[k2]:
            return False
    return True

"""Permutations"""

from itertools import permutations as perm


def permutations(string):
    return set(["".join(y for y in x) for x in list(perm(string))])

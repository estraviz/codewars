"""Club Doorman"""

from itertools import groupby
from string import ascii_lowercase


def pass_the_door_man(word):
    rep = [lst[0] for lst in get_groups_list(word) if len(lst) > 1][0]
    return (ascii_lowercase.index(rep) + 1) * 3


def get_groups_list(word):
    return [list(g) for k, g in groupby(word)]

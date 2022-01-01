# Pair of gloves
from collections import Counter


def number_of_pairs(gloves):
    return sum(v // 2 for v in Counter(gloves).values())

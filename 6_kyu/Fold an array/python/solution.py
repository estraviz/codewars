"""Fold an array"""

import operator


def fold_array(array, runs):
    folded = array.copy()

    for _ in range(runs):
        mid = len(folded) // 2
        odd = len(folded) % 2

        first = folded[:mid if odd else mid+1]
        second = folded[mid+1 if odd else mid:][::-1]

        folded = list(map(operator.add, first, second)) + ([folded[mid]] if odd else [])
    return folded

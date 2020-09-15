"""String array duplicates
"""

import itertools as it


def dup(arr):
    return ["".join(chr for chr, group in it.groupby(word)) for word in arr]

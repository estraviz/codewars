"""Find the missing term in an Arithmetic Progression"""

from collections import Counter


def find_missing(sequence):
    diffs = [y - x for x, y in zip(sequence, sequence[1:])]
    count = dict(Counter(diffs))
    step, outlier = max(count, key=count.get), min(count, key=count.get)
    return sequence[diffs.index(outlier) + 1] - step

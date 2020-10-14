"""Sum of array singles
"""

from collections import Counter


def repeats(arr):
    return sum(key for key, value in Counter(arr).items() if value == 1)

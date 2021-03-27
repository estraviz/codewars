"""Greed is Good"""

from collections import Counter


def score(dice):
    return 10 * sum(
        10 * (v // 3) * {1: 10}.get(k, k) + (v % 3) * {1: 10, 5: 5}.get(k, 0)
        for k, v in Counter(dice).items()
    )

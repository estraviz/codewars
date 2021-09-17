"""Throwing Darts"""


def score_throws(radii):
    res = 0
    if not radii:
        return res
    if all(r < 5 for r in radii):
        res += 100
    return res + sum(
        10 if 0 <= r < 5 else 5 if 5 <= r <= 10 else 0 for r in radii
        )

"""
Maximum Length Difference
"""


def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    lengths_a1, lengths_a2 = lengths(a1), lengths(a2)
    return max(
        max(lengths_a1) - min(lengths_a2),
        max(lengths_a2) - min(lengths_a1), 0)


def lengths(string):
    return [len(chr) for chr in string]

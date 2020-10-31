"""Basic Sequence Practice
"""


def sum_of_n(n):
    return [(1 if n > 0 else -1) * sum(range(abs(i) + 1)) for i in range(abs(n) + 1)]

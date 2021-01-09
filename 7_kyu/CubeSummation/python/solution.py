"""CubeSummation"""


def cube_sum(n, m):
    return sum(x ** 3 for x in range(min(n, m) + 1, max(n, m) + 1))

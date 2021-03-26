"""Functional Addition"""


def add(n):
    def add_n(k):
        return n + k
    return add_n

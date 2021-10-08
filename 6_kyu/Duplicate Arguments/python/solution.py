"""Duplicate Arguments"""


def solution(*args):
    return not(len(args) == len(set(args)))

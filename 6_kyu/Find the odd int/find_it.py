"""Find the odd int
"""
from collections import Counter


def find_it(seq):
    for key, value in Counter(seq).items():
        if value % 2 == 1:
            return key

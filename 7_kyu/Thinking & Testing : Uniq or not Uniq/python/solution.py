"""Thinking & Testing : Uniq or not Uniq"""

from itertools import chain


def lets_test_it(list1, list2):
    return sorted(chain(set(list1), set(list2)))

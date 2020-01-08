"""
Enumerable Magic #30 - Split that Array!
"""

from itertools import filterfalse


def partition(arr, classifier_method):
    return list(filter(classifier_method,
                       arr)), list(filterfalse(classifier_method, arr))

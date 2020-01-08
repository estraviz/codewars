"""
Enumerable Magic #30 - Split that Array!
"""


def partition(arr, classifier_method):
    lst = list(filter(classifier_method, arr))
    return lst, [item for item in arr if item not in lst]

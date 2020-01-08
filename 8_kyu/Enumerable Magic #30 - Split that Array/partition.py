"""
Enumerable Magic #30 - Split that Array!
"""


def partition(arr, classifier_method):
    first, second = [], []
    for x in arr:
        if classifier_method(x):
            first.append(x)
        else:
            second.append(x)
    return first, second

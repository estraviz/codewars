"""Counting Array Elements"""


def count(array):
    return dict(list((word, array.count(word)) for word in array))

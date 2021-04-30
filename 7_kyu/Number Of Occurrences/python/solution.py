"""Number Of Occurrences"""

from collections import Counter


def number_of_occurrences(element, sample):
    return Counter(sample).get(element, 0)

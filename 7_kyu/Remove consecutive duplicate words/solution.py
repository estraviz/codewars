"""Remove consecutive duplicate words
"""

from itertools import groupby


def remove_consecutive_duplicates(s):
    return " ".join(word for word, _ in groupby(s.split(" ")))

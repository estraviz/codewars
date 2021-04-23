"""Adjacent repeated words in a string"""

from itertools import groupby


def count_adjacent_pairs(st):
    return sum(1 for _, g in groupby(st.lower().split()) if len(list(g)) > 1)

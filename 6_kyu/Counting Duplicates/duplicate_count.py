"""Counting Duplicates
"""
from collections import Counter


def duplicate_count(text):
    return sum(1 for key, value in Counter(text.lower()).items() if value > 1)

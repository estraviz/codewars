"""
Detect Pangram
"""

from string import ascii_lowercase as ascii_low
from collections import Counter


def is_pangram(s):
    count = Counter(c for c in s.lower() if c in ascii_low)
    return all(v >= 1 for v in count.values()) and len(count) == len(ascii_low)

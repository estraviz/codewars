"""
Detect Pangram
"""

from string import ascii_lowercase


def is_pangram(s):
    return set(ascii_lowercase).issubset(s.lower())

"""Alphabetical Addition"""

from string import ascii_lowercase as chars


def add_letters(*letters):
    return chars[int(sum(chars.index(c) + 1 for c in letters) % len(chars)) - 1]

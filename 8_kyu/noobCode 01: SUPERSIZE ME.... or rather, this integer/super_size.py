"""
noobCode 01: SUPERSIZE ME.... or rather, this integer!
"""


def super_size(n):
    return int("".join(sorted([c for c in str(n)], reverse=True)))

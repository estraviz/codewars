"""
Simple Fun #87: Shuffled Array
"""


def shuffled_array(s):
    for i, val in enumerate(s):
        if sum(s[:i] + s[i+1:]) == val:
            return sorted(s[:i] + s[i+1:])

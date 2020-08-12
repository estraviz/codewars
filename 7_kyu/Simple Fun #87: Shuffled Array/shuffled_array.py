"""
Simple Fun #87: Shuffled Array
"""


def shuffled_array(s):
    s.remove(sum(s)//2)
    return sorted(s)


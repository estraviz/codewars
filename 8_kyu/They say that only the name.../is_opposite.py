"""
They say that only the name is long enough to attract attention.
They also said that only a simple Kata will have someone to solve it series #1:
Are they opposite?
"""


def is_opposite(s1, s2):
    return False if not s1 else s1 == s2.swapcase()

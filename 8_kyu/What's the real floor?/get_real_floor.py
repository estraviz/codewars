"""
What's the real floor?
"""


def get_real_floor(n):
    return n - 2 if n >= 13 else n - 1 if n > 0 else n

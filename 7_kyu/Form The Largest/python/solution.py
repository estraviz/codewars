"""
Form The Largest
"""


def max_number(n):
    return int("".join(sorted(str(n), reverse=True)))

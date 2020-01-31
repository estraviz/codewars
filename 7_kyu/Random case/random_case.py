"""
Random case
"""

from random import choice


def random_case(x):
    return "".join(choice([c.lower(), c.upper()]) for c in x)

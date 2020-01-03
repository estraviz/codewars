"""
Heads and Legs
"""


def animals(heads, legs):
    return (2 * heads - legs / 2,
            legs / 2 - heads) if is_valid(2 * heads - legs / 2) and is_valid(
                legs / 2 - heads) else "No solutions"


def is_valid(x):
    return x >= 0 and x == int(x)

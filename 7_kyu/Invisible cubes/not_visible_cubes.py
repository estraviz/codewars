"""
Invisible cubes
"""


def not_visible_cubes(n):
    return 0 if n < 3 else (n - 2)**3

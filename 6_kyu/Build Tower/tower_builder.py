"""
Build Tower
"""


def tower_builder(n_floors):
    return [
        (n_floors - n - 1) * ' ' + (2 * n + 1) * '*' + (n_floors - n - 1) * ' '
        for n in range(n_floors)
    ]

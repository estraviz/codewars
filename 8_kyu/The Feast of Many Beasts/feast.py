"""The Feast of Many Beasts
"""


def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])

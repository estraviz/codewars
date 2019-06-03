"""The Feast of Many Beasts
"""


def feast(beast, dish):
    return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False

"""
Testing 1-2-3
"""


def number(lines):
    return ["{}: {}".format(i + 1, elem) for i, elem in enumerate(lines)]

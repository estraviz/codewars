"""
Will there be enough space?
"""


def enough(cap, on, wait):
    return 0 if on + wait <= cap else on + wait - cap

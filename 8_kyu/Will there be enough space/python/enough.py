"""
Will there be enough space?
"""


def enough(cap, on, wait):
    return max(0, wait - (cap - on))

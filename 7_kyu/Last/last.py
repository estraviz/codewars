"""Last
"""


def last(*args):
    try:
        return args[-1][-1]
    except Exception:
        return args[-1]

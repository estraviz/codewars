"""Last
"""


def last(*args):
    try:
        return args[-1][-1]
    except:
        return args[-1]

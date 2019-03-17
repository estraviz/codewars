"""Last
"""


def last(*args):
    if len(args) == 1:
        try:
            last = args[0][-1]
            return last
        except TypeError:
            return args[0]
    return args[-1]

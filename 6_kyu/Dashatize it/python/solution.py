"""Dashatize it"""


DASH = '-'
EMPTY = ''


def dashatize(n):
    if n is None:
        return "None"

    try:
        str_n = str(abs(n))
        return "".join([DASH + x + DASH if is_odd(x) else x for x in str_n]).replace("--", DASH).lstrip(DASH).rstrip(DASH)
    except TypeError:
        return EMPTY


def is_odd(x):
    return int(x) in (1, 3, 5, 7, 9)

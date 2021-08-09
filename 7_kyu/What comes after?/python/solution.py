"""What comes after?"""

import re


def comes_after(st, letter):
    found = [c.start() for c in re.finditer(letter, st, re.IGNORECASE)]
    return "".join(get_next_char(i, st) for i in found
                   if is_at_most_prev_to_last(i, st) and is_next_alpha(i, st))


def is_at_most_prev_to_last(i, st):
    return i < len(st) - 1


def get_next_char(i, st):
    return st[i + 1]


def is_next_alpha(i, st):
    return get_next_char(i, st).isalpha()

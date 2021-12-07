# Switcheroo
import re


def switcheroo(s):
    a_matches = get_matches('a', s)
    b_matches = get_matches('b', s)

    s = do_replacement('b', a_matches, list(s))
    s = do_replacement('a', b_matches, list(s))
    return s


def get_matches(substr, str):
    matches = re.finditer(substr, str)
    return [match.start() for match in matches]


def do_replacement(chr, positions, lst):
    for position in positions:
        lst[position] = chr
    return "".join(lst)

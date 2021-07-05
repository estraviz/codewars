"""String Matcher"""

from collections import Counter


def is_matching(st, st1, st2):
    st_in = clean(st)
    st_out = clean(st1 + st2)
    return Counter(st_in) == Counter(st_out)


def clean(string):
    return "".join(x.lower() for x in string.replace(" ", ""))

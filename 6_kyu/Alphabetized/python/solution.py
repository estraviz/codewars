"""Alphabetized"""


def alphabetized(s):
    return "".join(sorted(filter(str.isalpha, s), key=str.upper))

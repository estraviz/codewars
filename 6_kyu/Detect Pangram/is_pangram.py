"""
Detect Pangram
"""

from string import ascii_letters


def is_pangram(s):
    dic = dict((chr.lower(), 0) for chr in ascii_letters)
    for c in s.lower():
        if c in dic.keys():
            dic[c] += 1
    return all(value >= 1 for value in dic.values())

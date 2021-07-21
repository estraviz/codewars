"""Consonant value"""

from string import ascii_letters


def solve(s):
    highest = 0
    temp = 0
    for c in s:
        if c in 'aeiou':
            if temp:
                highest = max(temp, highest)
                temp = 0
        else:
            temp += ascii_letters.index(c) + 1
    return max(temp, highest)

"""
Mexican Wave
"""

from string import ascii_lowercase


def wave(str):
    lst = []
    i = 0
    for letter in str:
        if letter in ascii_lowercase:
            lst.append(''.join(str[:i] + str[i].capitalize() + str[i + 1:]))
        i += 1
    return lst

"""
Simple Fun #114: "abacaba"
"""

from string import ascii_lowercase


def abacaba(k):
    str = ascii_lowercase[0]
    for i in range(1, 26):
        str = str + ascii_lowercase[i] + str
    return str[k - 1]

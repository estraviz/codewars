"""Break camelCase"""

from string import ascii_uppercase


def solution(s):
    return "".join(c if c not in ascii_uppercase else " " + c for c in s)

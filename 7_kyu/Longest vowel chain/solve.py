"""
Longest vowel chain
"""

import re


def solve(s):
    return max(len(x) for x in re.findall(r"[aeiou]+", s))

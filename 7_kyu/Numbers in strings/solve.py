"""
Numbers in strings
"""

import re


def solve(s):
    return max(map(int, re.findall(r'\d+', s)))

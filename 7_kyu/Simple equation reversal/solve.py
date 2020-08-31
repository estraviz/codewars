"""Simple equation reversal
"""

import re


def solve(eq):
    arr = re.split(r'(\D)', eq)
    return ''.join(arr[::-1])

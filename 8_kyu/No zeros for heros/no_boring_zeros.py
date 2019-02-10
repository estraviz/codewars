"""No zeros for heros
"""
import re


def no_boring_zeros(n):
    try:
        return int(re.sub(r'0*$', '', str(n)))
    except ValueError:
        return 0

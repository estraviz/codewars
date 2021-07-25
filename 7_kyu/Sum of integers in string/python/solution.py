"""Sum of integers in string"""

import re


def sum_of_integers_in_string(s):
    return sum(int(x) for x in (re.findall(r'(\d+)', s)))

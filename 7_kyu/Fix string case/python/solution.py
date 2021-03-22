"""Fix string case"""

from string import ascii_lowercase as asc_low, ascii_uppercase as asc_upp


def solve(s):
    lower, upper = sum_case(s, asc_low), sum_case(s, asc_upp)
    return s.lower() if lower >= upper else s.upper()


def sum_case(s, case):
    return sum(1 for x in s if x in case)

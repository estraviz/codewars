"""
Zero Terminated Sum
"""


def largest_sum(s):
    return max(sum(int(x) for x in arr) for arr in s.split('0'))

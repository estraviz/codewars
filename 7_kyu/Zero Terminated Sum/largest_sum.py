"""
Zero Terminated Sum
"""


def largest_sum(s):
    max_sum = 0
    for arr in s.split('0'):
        aux_sum = sum(int(x) for x in arr)
        if aux_sum > max_sum:
            max_sum = aux_sum
    return max_sum

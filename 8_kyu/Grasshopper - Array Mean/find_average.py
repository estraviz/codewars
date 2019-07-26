"""
Grasshopper - Array Mean
"""


def find_average(nums):
    return float(sum(nums))/max(1, len(nums))

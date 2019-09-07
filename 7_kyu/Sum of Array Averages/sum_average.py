"""
Sum of Array Averages
"""

from statistics import mean
from math import floor


def sum_average(arr):
    return floor(sum(mean(x) for x in arr))

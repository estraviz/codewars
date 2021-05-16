"""Largest pair sum in array"""

import heapq


def largest_pair_sum(numbers):
    return sum(heapq.nlargest(2, numbers))

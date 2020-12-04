"""Sum - Square Even, Root Odd"""

from math import sqrt


def sum_square_even_root_odd(nums):
    return round(sum(x ** 2 if x % 2 == 0 else sqrt(x) for x in nums), 2)

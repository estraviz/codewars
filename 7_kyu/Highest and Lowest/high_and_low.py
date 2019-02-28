"""Highest and Lowest
"""


def high_and_low(numbers):
    list_ = [int(num) for num in numbers.split()]
    return f"{max(list_)} {min(list_)}"

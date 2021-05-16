"""Largest pair sum in array"""


def largest_pair_sum(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0] + sorted_numbers[1]

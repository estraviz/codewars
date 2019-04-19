"""Average string
"""
from statistics import mean


def average_string(s):
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    inv_numbers = {v: k for k, v in numbers.items()}
    try:
        accum = [numbers[num] for num in s.split()]
        return inv_numbers[int(mean(accum))]
    except (ValueError, KeyError):
        return 'n/a'

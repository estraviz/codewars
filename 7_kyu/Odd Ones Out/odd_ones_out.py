"""
Odd Ones Out!
"""


def odd_ones_out(numbers):
    return [number for number in numbers if numbers.count(number) % 2 == 0]

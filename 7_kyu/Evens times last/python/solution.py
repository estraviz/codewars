"""Evens times last"""


def even_last(numbers):
    return 0 if not numbers else numbers[-1] * sum(numbers[::2])

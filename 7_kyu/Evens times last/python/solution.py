"""Evens times last"""


def even_last(numbers):
    return 0 if not numbers else sum(num for i, num in enumerate(numbers) if i % 2 == 0) * numbers[-1]

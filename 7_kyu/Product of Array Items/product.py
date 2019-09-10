"""
Product of Array Items
"""

from functools import reduce


def product(numbers):
    return None if not numbers else reduce(lambda x, y: x * y, numbers)

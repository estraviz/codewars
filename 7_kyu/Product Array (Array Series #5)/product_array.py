"""
Product Array (Array Series #5)
"""

from operator import mul
from functools import reduce


def product_array(numbers):
    return [reduce(mul, numbers) / num for num in numbers]

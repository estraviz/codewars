"""Smallest value of an array"""


def find_smallest(numbers, to_return):
    return {"value": min(numbers), "index": numbers.index(min(numbers))}.get(to_return)

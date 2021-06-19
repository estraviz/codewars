"""Number Zoo Patrol"""


def find_missing_number(numbers):
    return next(iter(set(numbers) ^ set(range(1, len(numbers)+2))))

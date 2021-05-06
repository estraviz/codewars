"""Sum of Minimums!"""


def sum_of_minimums(numbers):
    return sum(min(item) for item in numbers)

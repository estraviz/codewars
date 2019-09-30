"""
Two Sum
"""


def two_sum(numbers, target):
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i != j and num1 + num2 == target:
                return [i, j]

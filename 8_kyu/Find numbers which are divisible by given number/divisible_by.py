"""Find numbers which are divisible by given number
"""


def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]

"""Calculate Variance"""


def variance(numbers):
    mean = sum(numbers) / len(numbers)
    return sum((number - mean) ** 2 for number in numbers) / len(numbers)

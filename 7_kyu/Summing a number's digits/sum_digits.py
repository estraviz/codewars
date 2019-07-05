"""
Summing a number's digits
"""


def sum_digits(number):
    return sum(int(num) for num in str(abs(number)))

"""Validate Credit Card Number"""


def validate(n):
    numbers = list(int(digit) for digit in str(n))
    double_every_other = []
    for i, num in enumerate(numbers):
        if len(numbers) % 2 == i % 2:
            num *= 2
            if num > 9:
                num = sum(int(x) for x in str(num))
        double_every_other.append(num)
    return sum(double_every_other) % 10 == 0

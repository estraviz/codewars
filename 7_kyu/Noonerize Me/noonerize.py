"""Noonerize Me
"""


def noonerize(numbers):
    if any(not isinstance(n, int) for n in numbers):
        return "invalid array"
    return abs(int(str(numbers[1])[0] + str(numbers[0])[1:]) - int(str(numbers[0])[0] + str(numbers[1])[1:]))

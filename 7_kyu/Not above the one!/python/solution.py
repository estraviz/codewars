"""Not above the one!"""


def binary_cleaner(seq):
    first, second = [], []
    for index, number in enumerate(seq):
        if number < 2:
            first.append(number)
        if number > 1:
            second.append(index)
    return first, second

"""IQ Test
"""


def iq_test(numbers):
    evenness = [int(num) % 2 for num in numbers.split()]
    return evenness.index(1 if sum(evenness) == 1 else 0) + 1

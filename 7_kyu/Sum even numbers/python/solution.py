"""Sum even numbers"""


def sum_even_numbers(seq):
    return sum(x for x in seq if x % 2 == 0)

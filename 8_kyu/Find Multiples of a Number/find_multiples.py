"""
Find Multiples of a Number
"""


def find_multiples(integer, limit):
    return list(
        filter(lambda x: x <= limit,
               (integer * k for k in range(1, limit + 1))))

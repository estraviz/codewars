"""Bit Counting
"""


def count_bits(n):
    return sum(int(digit) for digit in bin(n)[2:])

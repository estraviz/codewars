"""Delta Bits"""

from itertools import zip_longest


def convert_bits(a, b):
    return sum(
        x != y
        for x, y in zip_longest(bin(a)[2:][::-1], bin(b)[2:][::-1], fillvalue="0")
    )

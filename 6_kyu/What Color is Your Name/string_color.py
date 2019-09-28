"""
What Color is Your Name?
"""

from functools import reduce


def string_color(name):
    if not name or len(name) < 2:
        return None

    ascii_values = [ord(letter) for letter in name]

    first = check_leading_zero(hex(sum(ascii_values) % 256)[2:])
    second = check_leading_zero(
        hex(reduce(lambda x, y: x * y, ascii_values) % 256)[2:])
    third = check_leading_zero(
        hex(abs(ascii_values[0] - sum(ascii_values[1:])) % 256)[2:])

    return ''.join([first, second, third])


def check_leading_zero(hex_num):
    return str(hex_num).rjust(2, '0').upper()

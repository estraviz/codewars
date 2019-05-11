"""Printer Error
"""


def printer_error(s):
    return f"{sum([1 for letter in s if ord(letter) not in range(ord('a'), ord('n'))])}/{len(s)}"

"""
Perfect squares, perfect fun
"""

from math import sqrt


def square_it(digits):
    digits = str(digits)
    length = len(digits)
    block = int(sqrt(length))
    return '\n'.join(digits[i:i + block] for i in range(
        0, length, block)) if block**2 == length else "Not a perfect square!"

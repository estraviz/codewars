"""
What Color is Your Name?
"""

from functools import reduce


def string_color(name):
    if len(name) >= 2:
        asciis = [ord(letter) for letter in name]
        return ''.join(
            map(lambda x: f'{x % 256:02X}', [
                sum(asciis),
                reduce(lambda x, y: x * y, asciis),
                abs(asciis[0] - sum(asciis[1:]))
            ]))

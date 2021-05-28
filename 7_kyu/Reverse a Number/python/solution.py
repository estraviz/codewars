"""Reverse a Number"""


def reverse_number(n):
    return (-1 if n < 0 else 1) * int(str(abs(n))[::-1])

"""Is a number prime?
"""
from math import sqrt


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

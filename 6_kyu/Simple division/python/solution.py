# Simple division
from math import sqrt


def solve(a, b):
    divisors = [d for d in range(2, b//2) if b % d == 0 and is_prime(d)]
    return False if not divisors else all(a % d == 0 for d in divisors)


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

# Next Prime
from math import sqrt


def next_prime(n):
    if n < 2:
        return 2
    while True:
        n += 1
        if is_prime(n):
            return n


def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

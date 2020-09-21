"""
Filling an array (part 2)
"""

from random import randint


def squares(n):
    return [(i + 1)**2 for i in range(n)]


def num_range(n, start, step):
    return [start + (i - start)*step for i in range(start, start + n)]


def rand_range(n, mn, mx):
    return [randint(mn, mx) for _ in range(n)]


def primes(n):
    output = []
    num = 2
    while len(output) < n:
        is_prime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            output.append(num)
        num += 1
    return output

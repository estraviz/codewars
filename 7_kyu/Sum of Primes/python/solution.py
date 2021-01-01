"""Sum of Primes"""


from math import sqrt


def sum_primes(lower, upper):
    _sum = 0
    if lower > upper:
        return _sum
    num = lower
    while num <= upper:
        if is_prime(num):
            _sum += num
        num += 1
    return _sum


def is_prime(n):
    if is_two_or_greater(n) and is_a_whole_number(n):
        for i in range(2, int(sqrt(n)) + 1):
            if is_divisible_by(n, i):
                return False
        return True
    else:
        return False


def is_two_or_greater(n):
    return n >= 2


def is_a_whole_number(n):
    return n % 1 == 0


def is_divisible_by(n, i):
    return n % i == 0

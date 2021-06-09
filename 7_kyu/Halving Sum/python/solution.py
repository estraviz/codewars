"""Halving Sum"""


def halving_sum(n):
    sum = 0
    while n >= 1:
        sum += n
        n //= 2
    return sum

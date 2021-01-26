"""Count the divisors of a number"""


def divisors(n):
    return sum(1 for x in range(1, n + 1) if n % x == 0)

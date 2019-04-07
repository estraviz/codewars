"""Collatz
"""


def collatz(n):
    if n == 1:
        return '1'
    else:
        if n % 2 == 0:
            result = n//2
        else:
            result = 3*n + 1
    return '{}->{}'.format(n, collatz(result))

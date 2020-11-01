"""Reverser
"""


def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    i = 0
    coefs = []
    while n > 0:
        rem = n % 10
        n = n // 10
        coefs.append(rem)
        i += 1
    return sum(10**i * k for i, k in enumerate(coefs[::-1]))

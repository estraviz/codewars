"""Sum of Digits / Digital Root
"""


def digital_root(n):
    return n if n < 10 else digital_root(sum(int(x) for x in str(n)))

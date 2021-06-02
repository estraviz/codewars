"""Find the nth Digit of a Number"""


def find_digit(num, nth):
    return -1 if nth <= 0 else int(str(abs(num)).zfill(nth)[::-1][nth-1])

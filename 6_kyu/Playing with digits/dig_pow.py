"""Playing with digits
"""


def dig_pow(n, p):
    sum_of_powers = 0
    for digit in str(n):
        sum_of_powers += int(digit)**p
        p += 1
    return sum_of_powers // n if sum_of_powers % n == 0 else -1

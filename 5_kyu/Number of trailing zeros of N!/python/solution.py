"""Number of trailing zeros of N!"""


def zeros(n):
    count = 0
    while n / 5 >= 1:
        count += n // 5
        n /= 5
    return count

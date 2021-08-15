"""Especially Joyful Numbers"""


def number_joy(n):
    s = get_digit_sum(n)
    if is_harshad(n, s) and is_digit_sum_times_reversed_original(n, s):
        return True
    return False


def get_digit_sum(n):
    return sum(int(x) for x in str(n))


def is_harshad(n, s):
    return n % s == 0


def is_digit_sum_times_reversed_original(n, s):
    return s * int(str(s)[::-1]) == n

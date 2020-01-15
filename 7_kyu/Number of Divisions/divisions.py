"""
Number of Divisions
"""


def divisions(n, divisor):
    count = 0
    while n >= divisor:
        n /= divisor
        count += 1
    return count

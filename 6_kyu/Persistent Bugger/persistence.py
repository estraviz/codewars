"""Persistent Bugger
"""
from functools import reduce


def persistence(num):
    if num < 10:
        return 0
    count = 0
    while True:
        num_list = [int(n) for n in str(num)]
        num = reduce(lambda x, y: x*y, num_list)
        count += 1
        if num < 10:
            break
    return count

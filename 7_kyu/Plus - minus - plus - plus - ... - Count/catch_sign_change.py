"""
Plus - minus - plus - plus - ... - Count
"""


def catch_sign_change(lst):
    count = 0
    for i, num in enumerate(lst):
        if i != 0:
            if sign(num) != sign(prev):
                count += 1
        prev = num
    return count


def sign(x):
    return -1 if x < 0 else 1

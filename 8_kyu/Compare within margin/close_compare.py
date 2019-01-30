"""Compare within margin
"""


def close_compare(a, b, margin=0):
    return 0 if margin >= abs(a - b) else -1 if a < b else 1

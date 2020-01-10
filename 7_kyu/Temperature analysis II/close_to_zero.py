"""
Temperature analysis II
"""


def close_to_zero(t):
    return 0 if not t else min([int(x) for x in t.split()],
                               key=lambda x: (abs(x), -x))

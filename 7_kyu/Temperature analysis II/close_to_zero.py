"""
Temperature analysis II
"""


def close_to_zero(t):
    if not t:
        return 0
    t = [int(x) for x in t.split()]
    close = min(t, key=lambda x: abs(x))
    return abs(close) if close < 0 and abs(close) in t else close

"""
Temperature analysis II
"""


def close_to_zero(t):
    close = None
    if t:
        for x in (int(x) for x in t.split()):
            if not close or abs(x) < abs(close) or x == -1 * close and x > 0:
                close = x
                if close == 0:
                    break
    return close or 0

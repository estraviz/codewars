"""Luck check"""


def luck_check(s):
    try:
        left, right = len(s) // 2, (len(s) + 1) // 2
        return sum(int(x) for x in s[:left]) == sum(int(x) for x in s[right:])
    except Exception:
        raise ValueError

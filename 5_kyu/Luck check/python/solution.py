"""Luck check"""


def luck_check(string):
    try:
        int(string)
        mid = len(string) // 2
        left = string[:mid]
        right = string[mid + 1:] if len(string) % 2 else string[mid:]
        return sum(int(x) for x in left) == sum(int(x) for x in right)
    except Exception:
        raise ValueError

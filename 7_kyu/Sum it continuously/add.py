"""
Sum it continuously
"""


def add(l):
    new_l = []
    accum = 0
    if not isinstance(l, list):
        return 'Invalid input'
    for num in l:
        if isinstance(num, int):
            accum += num
            new_l.append(accum)
        else:
            return 'Invalid input'
    return new_l

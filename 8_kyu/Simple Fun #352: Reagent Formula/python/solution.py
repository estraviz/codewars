"""Simple Fun #352: Reagent Formula"""


def is_valid(arr):
    return False if both(arr, 1, 2) or \
                    both(arr, 3, 4) or \
                    one_only(arr, 5, 6) or \
                    one_only(arr, 6, 5) or \
                    neither(arr, 7, 8) else True


def both(arr, a, b):
    return a in arr and b in arr


def one_only(arr, a, b):
    return a in arr and b not in arr


def neither(arr, a, b):
    return a not in arr and b not in arr

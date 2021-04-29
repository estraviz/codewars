"""Most digits"""


def find_longest(arr):
    return int(max((str(x) for x in arr), key=len))

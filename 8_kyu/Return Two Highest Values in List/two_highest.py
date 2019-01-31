from heapq import nlargest


def two_highest(arg1):
    if len(arg1) == 0:
        return arg1
    if all(isinstance(x, int) for x in arg1):
        return nlargest(2, set(arg1))
    return False

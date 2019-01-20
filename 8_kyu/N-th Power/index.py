"""N-th Power
"""


def index(array, n):
    return -1 if n > len(array) else array[n]**n

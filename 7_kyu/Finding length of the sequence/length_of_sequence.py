"""
Finding length of the sequence
"""


def length_of_sequence(arr, n):
    if arr.count(n) != 2:
        return 0
    for i, c in enumerate(arr):
        if n == c:
            try:
                return i - first + 1
            except:
                first = i

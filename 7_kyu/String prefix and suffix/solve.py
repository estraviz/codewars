"""
String prefix and suffix
"""


def solve(st):
    ind = len(st) // 2
    while ind > 0:
        if st[:ind] == st[-ind:]:
            return ind
        ind -= 1
    else:
        return 0

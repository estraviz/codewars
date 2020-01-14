"""
Simple rotated palindromes
"""


def solve(st):
    for _ in st:
        st = st[-1] + st[:-1]
        if st == st[::-1]:
            return True
    return False

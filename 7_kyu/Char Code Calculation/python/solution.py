"""Char Code Calculation"""


def calc(x):
    total1 = "".join(str(ord(c)) for c in x)
    total2 = total1.replace("7", "1")
    return sum(int(c) for c in total1) - sum(int(c) for c in total2)

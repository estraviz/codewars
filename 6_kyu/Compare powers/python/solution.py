# Compare powers
from math import log


def compare_powers(n1, n2):
    [b1, e1], [b2, e2] = n1, n2
    l1, l2 = e1*log(b1), e2*log(b2)
    return -1 if l1 > l2 else 0 if l1 == l2 else 1

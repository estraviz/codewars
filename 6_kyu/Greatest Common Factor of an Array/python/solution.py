"""Greatest Common Factor of an Array"""


def greatest_common_factor(seq):
    temp = seq[0]
    for k in seq[1:]:
        temp = gcd(temp, k)
    return temp


def gcd(i, j):
    return j if i % j == 0 else gcd(j, i % j)

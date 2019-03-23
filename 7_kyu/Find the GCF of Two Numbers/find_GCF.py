"""Find the GCF of Two Numbers
"""


def find_GCF(a, b):
    if b == 0:
        return a
    return find_GCF(b, a % b)

"""Which string is worth more?"""


def highest_value(a, b):
    return a if worth(a) >= worth(b) else b


def worth(z):
    return sum(ord(x) for x in z)

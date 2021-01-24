"""Weight for weight"""

from operator import itemgetter


def order_weight(strng):
    weights = sorted(
        [
            (weight, sum(int(digit) for digit in list(weight)))
            for weight in strng.split(" ")
        ],
        key=lambda x: (x[1], x[0]),
    )
    return " ".join(map(itemgetter(0), weights))

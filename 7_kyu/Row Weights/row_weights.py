"""
Row Weights
"""


def row_weights(array):
    odd = []
    even = []
    for i, elem in enumerate(array):
        if (i + 1) % 2 == 0:
            even.append(elem)
        else:
            odd.append(elem)
    return (sum(odd), sum(even))

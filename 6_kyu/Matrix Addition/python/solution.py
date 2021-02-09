"""Matrix Addition"""


def matrix_addition(a, b):
    return [list(map(sum, zip(*row))) for row in zip(a, b)]

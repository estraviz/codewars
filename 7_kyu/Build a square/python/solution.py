"""Build a square"""


def generate_shape(n):
    return '\n'.join('+' * n for i in range(1, n+1))

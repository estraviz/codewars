"""Calculate the function f(x) for a simple linear sequence (Easy)
"""


def get_function(f):
    """Let's consider a linear relationship of the kind: y=A*x+B"""
    A, B = f[1] - f[0], f[0]

    for i, f_i in enumerate(f):
        if f_i != A*i + B:
            return 'Non-linear sequence'

    if B == 0:
        if A == 1:
            return 'f(x) = x'
        else:
            return 'f(x) = {}x'.format(A)

    if A == 0:
        return 'f(x) = {}'.format(B)

    if A == 1:
        return 'f(x) = x {} {}'.format(sign(B), abs(B))

    if A == -1:
        return 'f(x) = -x {} {}'.format(sign(B), abs(B))

    return 'f(x) = {}x {} {}'.format(A, sign(B), abs(B))


def sign(b):
    return '-' if b < 0 else '+'

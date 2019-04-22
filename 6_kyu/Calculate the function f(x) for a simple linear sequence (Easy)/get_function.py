"""Calculate the function f(x) for a simple linear sequence (Easy)
"""


def get_function(sequence):
    """Find a linear relationship of the kind: f = n*x + m"""
    m = sequence[0]
    n = sequence[1] - m

    if sequence[2] != n*2 + m or \
       sequence[3] != n*3 + m or \
       sequence[4] != n*4 + m:
        return 'Non-linear sequence'

    if n != 0:
        if m < 0:
            if n == 1:
                return "f(x) = x - {}".format(abs(m))
            return "f(x) = {}x - {}".format(n, abs(m))
        elif m > 0:
            if n == 1:
                return "f(x) = x + {}".format(m)
            return "f(x) = {}x + {}".format(n, m)
        else:
            if n == 1:
                return "f(x) = x"
            return "f(x) = {}x".format(n)
    return "f(x) = {}".format(m)

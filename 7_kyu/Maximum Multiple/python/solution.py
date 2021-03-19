"""Maximum Multiple"""


def max_multiple(divisor, bound):
    while bound >= divisor:
        if bound % divisor == 0:
            return bound
        bound -= 1

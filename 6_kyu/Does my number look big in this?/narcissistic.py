"""Does my number look big in this?
"""


def narcissistic(value):
    return sum([int(i)**len(str(value)) for i in str(value)]) == value

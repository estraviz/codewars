"""A function within a function
"""


def always(n=0):
    def never():
        return n
    return never

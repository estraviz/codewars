'''Stringy Strings
'''


def stringy(size):
    return "".join(str((i + 1) % 2) for i in range(size))

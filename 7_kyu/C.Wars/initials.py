"""
C.Wars
"""


def initials(name):
    words = name.split()
    return '.'.join([
        '.'.join(chr[0].upper() for chr in words[:-1]), words[-1].capitalize()
    ])

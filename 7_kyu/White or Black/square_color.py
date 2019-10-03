"""
White or Black?
"""


def square_color(file, rank):
    return 'white' if (ord(file) + rank) % 2 else 'black'

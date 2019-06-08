"""Add length
"""


def add_length(str_):
    return [" ".join([elem, str(len(elem))]) for elem in str_.split()]

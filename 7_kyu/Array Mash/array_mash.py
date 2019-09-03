"""
Array Mash
"""


def array_mash(a, b):
    output = []
    for elem_a, elem_b in zip(a, b):
        output.extend([elem_a, elem_b])
    return output

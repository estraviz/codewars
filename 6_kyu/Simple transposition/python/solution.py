"""Simple transposition"""


def simple_transposition(text):
    row_1 = ""
    row_2 = ""
    for i, c in enumerate(text):
        if i % 2 == 0:
            row_1 += c
        else:
            row_2 += c
    return row_1 + row_2

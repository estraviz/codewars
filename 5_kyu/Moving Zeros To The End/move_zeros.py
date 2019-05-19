"""Move Zeros To The End
"""


def move_zeros(array):
    clean, zeros = [], []
    for elem in array:
        if type(elem) in (int, float) and int(elem) == 0:
            zeros.append(0)
        else:
            clean.append(elem)
    return clean + zeros

"""Calculate String Rotation"""


def shifted_diff(first, second):
    if len(first) != len(second):
        return -1
    n = 0
    second_aux = second
    while first != second:
        second = second[1:] + second[0]
        if second == second_aux:
            return -1
        n += 1
    return n

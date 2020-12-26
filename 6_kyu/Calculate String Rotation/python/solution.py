"""Calculate String Rotation"""


def shifted_diff(first, second):
    return -1 if len(first) != len(second) else (second * 2).find(first)

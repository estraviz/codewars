"""
Rotate for a Max
"""


def max_rot(n):
    rotated, i = [n], 0
    while i < len(str(n)):
        n = rotate_left(n, i)
        rotated.append(n)
        i += 1
    return max(rotated)


def rotate_left(n, i):
    return int(str(n)[0:i] + str(n)[i + 1:] + str(n)[i:i + 1])

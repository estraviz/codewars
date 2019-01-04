'''Find out whether the shape is a cube
'''


def cube_checker(volume, side):
    return False if (volume <= 0 or side <= 0) else (volume == side ** 3)

"""Take a Ten Minute Walk
"""
from collections import Counter

NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'


def is_valid_walk(walk):
    return True if \
        is_len_of_walk_x(walk, 10) and \
        is_num_steps_equal(walk, NORTH, SOUTH) and \
        is_num_steps_equal(walk, EAST, WEST) else False


def is_len_of_walk_x(walk, x):
    return len(walk) == x


def is_num_steps_equal(walk, dir1, dir2):
    steps = Counter(walk)
    return steps[dir1] == steps[dir2]

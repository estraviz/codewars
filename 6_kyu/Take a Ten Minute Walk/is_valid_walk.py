"""Take a Ten Minute Walk
"""
from enum import Enum, unique


@unique
class Dir(Enum):
    NORTH = 'n'
    EAST = 'e'
    SOUTH = 's'
    WEST = 'w'


def is_valid_walk(walk):
    return True if is_len_of_walk(walk, 10) and is_back_to_start(walk) \
      else False


def is_len_of_walk(w, x):
    return len(w) == x


def is_back_to_start(w):
    return is_num_steps_equal(w, Dir.NORTH.value, Dir.SOUTH.value) and \
           is_num_steps_equal(w, Dir.EAST.value, Dir.WEST.value)


def is_num_steps_equal(w, dir1, dir2):
    return w.count(dir1) == w.count(dir2)

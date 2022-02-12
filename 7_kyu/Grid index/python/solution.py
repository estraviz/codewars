# Grid index
import itertools


def grid_index(grid, indexes):
    chars = list(itertools.chain.from_iterable(grid))
    return "".join(chars[i-1] for i in indexes)

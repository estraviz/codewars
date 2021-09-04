"""Find the Mine!"""

import numpy as np


def mineLocation(field):
    arr = np.array(field)
    mine = np.where(arr == 1)
    return [mine[0], mine[1]]

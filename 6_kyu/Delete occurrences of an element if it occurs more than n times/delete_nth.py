"""Delete occurrences of an element if it occurs more than n times
"""


import numpy as np


def delete_nth(order, max_e):
    counts, erase = {}, []
    for i, elem in enumerate(order):
        if elem not in counts:
            counts[elem] = 1
        else:
            counts[elem] += 1
            if counts[elem] > max_e:
                erase.append(i)
    return np.delete(order, erase).tolist()

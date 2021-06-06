"""Making Copies"""

import copy


def copy_list(lst):
    if not lst:
        raise Exception
    return copy.deepcopy(lst)

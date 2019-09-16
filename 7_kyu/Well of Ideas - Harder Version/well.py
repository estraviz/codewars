"""
Well of Ideas - Harder Version
"""

from itertools import chain


def well(arr):
    num_good = [
        elem.lower() if type(elem) == str else ''
        for elem in chain.from_iterable(arr)
    ].count('good')
    return {
        0: 'Fail!',
        1: 'Publish!',
        2: 'Publish!'
    }.get(num_good, 'I smell a series!')

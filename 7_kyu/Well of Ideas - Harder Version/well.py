"""
Well of Ideas - Harder Version
"""


def well(arr):
    count = [
        elem.lower() if type(elem) == str else '' for inner_arr in arr
        for elem in inner_arr
    ].count('good')
    return {
        0: 'Fail!',
        1: 'Publish!',
        2: 'Publish!'
    }.get(count, 'I smell a series!')

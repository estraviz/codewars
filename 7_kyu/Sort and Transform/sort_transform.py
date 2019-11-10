"""
Sort and Transform
"""


def sort_transform(arr):
    e1 = ''.join(get_word(arr))
    e2 = ''.join(get_word(sorted(arr)))
    e3 = ''.join(get_word(sorted(arr, reverse=True)))
    e4 = e2
    return '-'.join([e1, e2, e3, e4])


def compose_list(arr):
    return [arr[0], arr[1], arr[-2], arr[-1]]


def get_word(arr):
    return list(map(chr, compose_list(arr)))

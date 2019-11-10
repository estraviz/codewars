"""
Sort and Transform
"""


def sort_transform(arr):
    return '-'.join([
        get_word(arr),
        get_word(sorted(arr)),
        get_word(sorted(arr, reverse=True)),
        get_word(sorted(arr))
    ])


def get_word(arr):
    return ''.join(map(chr, [arr[0], arr[1], arr[-2], arr[-1]]))

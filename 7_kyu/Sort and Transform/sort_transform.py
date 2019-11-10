"""
Sort and Transform
"""


def sort_transform(arr):
    e1 = ''.join(compose_chr_list(arr))
    e2 = ''.join(compose_chr_list(sorted(arr)))
    e3 = ''.join(compose_chr_list(sorted(arr, reverse=True)))
    e4 = ''.join(compose_list(sorted([chr(x) for x in arr])))
    return '-'.join([e1, e2, e3, e4])


def compose_list(arr_aux):
    return [arr_aux[0], arr_aux[1], arr_aux[-2], arr_aux[-1]]


def compose_chr_list(arr):
    return [chr(arr[0]), chr(arr[1]), chr(arr[-2]), chr(arr[-1])]

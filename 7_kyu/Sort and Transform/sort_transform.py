"""
Sort and Transform
"""


def sort_transform(arr):
    arr_aux = arr
    new_arr = [chr(arr_aux[0]), chr(arr_aux[1]), chr(arr_aux[-2]), chr(arr_aux[-1])]
    part_one = ''.join(new_arr)

    arr_aux = sorted(arr)
    new_arr = [chr(arr_aux[0]), chr(arr_aux[1]), chr(arr_aux[-2]), chr(arr_aux[-1])]
    part_two = ''.join(new_arr)

    arr_aux = sorted(arr, reverse=True)
    new_arr = [chr(arr_aux[0]), chr(arr_aux[1]), chr(arr_aux[-2]), chr(arr_aux[-1])]
    part_three = ''.join(new_arr)

    arr_aux = sorted([chr(x) for x in arr])
    new_arr = [arr_aux[0], arr_aux[1], arr_aux[-2], arr_aux[-1]]
    part_four = ''.join(new_arr)

    return '-'.join([part_one, part_two, part_three, part_four])

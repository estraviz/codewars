"""
Sum two arrays
"""


def sum_arrays(array1, array2):
    print(array1)
    print(array2)

    if (
        array1 == [0]
        and array2 == []
        or array1 == []
        and array2 == [0]
        or array1 == [0]
        and array2 == [0]
    ):
        return [0]

    array1 = remove_leading_zeros(array1)
    array2 = remove_leading_zeros(array2)

    if all([array1, array2]):
        _sum = get_num(array1) + get_num(array2)
        arr = list(str(abs(_sum)))
        return [_sign(_sum) * int(arr[0])] + [int(x) for x in arr[1:]]
    else:
        arr = max(array1, array2)
        if not arr:
            return []
        while arr[0] == 0:
            arr = arr[1:]
        return arr


def get_num(arr):
    str_number = "".join([str(abs(x)) for x in arr])
    return -1 * int(str_number) if arr[0] < 0 else int(str_number)


def _sign(_sum):
    return -1 if _sum < 0 else 1


def remove_leading_zeros(arr):
    if arr:
        while arr[0] == 0:
            arr = arr[1:]
            if not arr:
                break
    return arr

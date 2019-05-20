"""Find the unique number
"""


def find_uniq(arr):
    if arr[0] == arr[1]:
        for n in arr[2:]:
            if n != arr[0]:
                return n
    if arr[0] == arr[2]:
        return arr[1]
    return arr[0]

"""
Nice Array
"""


def is_nice(arr):
    if arr:
        for i, elem in enumerate(arr):
            new_arr = arr.copy()
            new_arr.pop(i)
            if is_item_in_list(elem - 1, new_arr) or is_item_in_list(
                    elem + 1, new_arr):
                continue
            else:
                return False
        return True
    return False


def is_item_in_list(item, lst):
    try:
        pos = lst.index(item)
        return True
    except ValueError:
        return False

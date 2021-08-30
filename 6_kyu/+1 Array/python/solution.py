"""+1 Array"""


def up_array(arr):
    if not arr or any(x for x in arr if x < 0 or x > 9):
        return None
    return list(int(x) for x in str(int("".join(str(y) for y in arr)) + 1))

"""Is Integer Array?"""


def is_int_array(arr):
    return isinstance(arr, list) and all(
        isinstance(x, int) or
        isinstance(x, float) and x.is_integer() for x in arr
        )

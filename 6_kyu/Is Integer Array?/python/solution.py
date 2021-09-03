"""Is Integer Array?"""


def is_int_array(arr):
    return isinstance(arr, list) and all(
        x is not None and is_a_number(x) and has_no_decimals(x) for x in arr
        )


def is_a_number(x):
    return type(x) == int or type(x) == float


def has_no_decimals(x):
    return int(x) == x

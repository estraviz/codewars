"""Map function issue"""


def func(n):
    return int(n) % 2 == 0


def map(arr, somefunction):
    # note: Python already supports all this, we are just rewriting our own
    # map() function with some quirk and error message
    try:
        return [somefunction(n) for n in arr]
    except ValueError:
        return "array should contain only numbers"
    except TypeError:
        return "given argument is not a function"

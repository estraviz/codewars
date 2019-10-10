"""
Currying functions: multiply all elements in an array
"""


def multiply_all(arr):
    def multiply_array_by_scalar(num):
        return [num * elem for elem in arr]

    return multiply_array_by_scalar

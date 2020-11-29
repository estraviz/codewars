"""
Max-min arrays
"""


def solve(arr):
    arr_sorted = sorted(arr, reverse=True)
    output = []
    while arr_sorted:
        output.append(arr_sorted.pop(0))
        if arr_sorted:
            output.append(arr_sorted.pop(-1))
    return output

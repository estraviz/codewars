"""
Sub-array elements sum
"""


def elements_sum(arr, d=0):
    add, ind = 0, 1
    for elem in arr:
        try:
            add += elem[len(arr) - ind]
        except IndexError:
            add += d
        finally:
            ind += 1
    return add

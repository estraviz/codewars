"""Sum without highest and lowest number
"""


def sum_array(arr):
    return 0 if not arr else sum(sorted(arr)[1:-1])

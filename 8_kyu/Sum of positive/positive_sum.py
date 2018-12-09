'''Sum of positive
'''


def positive_sum(arr):
    return sum(x if x > 0 else 0 for x in arr)

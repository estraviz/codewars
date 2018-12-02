'''
Count of positives / sum of negatives
'''


def count_positives_sum_negatives(arr):
    return arr if arr == [] else \
        [sum(1 for num in arr if num > 0), sum(num for num in arr if num < 0)]

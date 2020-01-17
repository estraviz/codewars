"""
Diagonals sum
"""


def sum_diagonals(matrix):
    return sum(arr[i] + arr[len(arr) - i - 1] for i, arr in enumerate(matrix))

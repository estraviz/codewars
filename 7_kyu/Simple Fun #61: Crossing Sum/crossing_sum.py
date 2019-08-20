"""
Simple Fun #61: Crossing Sum
"""

import numpy as np


def crossing_sum(matrix, row, col):
    matrix = np.array(matrix)
    return matrix[row, :].sum() + matrix[:, col].sum() - matrix[row, col]

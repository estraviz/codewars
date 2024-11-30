"""Smallest unused ID
"""


def next_id(arr):
    current_id = 0
    while current_id in arr:
        current_id += 1
    return current_id

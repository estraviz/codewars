"""
    Computer problem series #1: Fill the Hard Disk Drive
"""


def save(sizes, hd):
    sum = 0
    for i, size in enumerate(sizes):
        sum += size
        if sum > hd:
            return i
    return len(sizes)

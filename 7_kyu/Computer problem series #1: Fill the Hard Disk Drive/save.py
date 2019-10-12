"""
    Computer problem series #1: Fill the Hard Disk Drive
"""


def save(sizes, hd):
    total = count = 0
    for size in sizes:
        total += size
        if total > hd:
            break
        count += 1
    return count

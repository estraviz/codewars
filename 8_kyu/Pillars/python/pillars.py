"""
Pillars
"""


def pillars(num_pill, dist, width):
    return 0 if num_pill <= 1 \
        else (num_pill - 1) * dist * 100 + (num_pill - 2) * width

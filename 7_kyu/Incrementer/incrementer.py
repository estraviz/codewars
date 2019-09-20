"""
Incrementer
"""


def incrementer(nums):
    return [(num + i) % 10 for i, num in enumerate(nums, 1)] if nums else []

"""
Incrementer
"""


def incrementer(nums):
    return [(num + i + 1) % 10 for i, num in enumerate(nums)] if nums else []

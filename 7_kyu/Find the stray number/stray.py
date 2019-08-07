"""
Find the stray number
"""


def stray(arr):
    num1, num2 = set(arr)
    return num1 if arr.count(num1) == 1 else num2

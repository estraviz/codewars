"""
Sum of Odd Cubed Numbers
"""


def cube_odd(arr):
    try:
        return sum(num**3 for num in arr if num % 2 == 1)
    except TypeError:
        return None

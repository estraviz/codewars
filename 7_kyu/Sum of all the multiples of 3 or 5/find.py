"""
Sum of all the multiples of 3 or 5
"""


def find(n):
    return sum([num for num in range(1, n+1) if num % 3 == 0 or num % 5 == 0])

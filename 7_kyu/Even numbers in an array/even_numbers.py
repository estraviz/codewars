"""Even numbers in an array
"""


def even_numbers(arr, n):
    return [num for num in arr if num % 2 == 0][-n:]

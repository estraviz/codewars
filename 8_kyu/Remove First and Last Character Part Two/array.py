"""
Remove First and Last Character Part Two
"""


def array(string):
    arr = [elem for elem in string.replace(' ', '').split(',')]
    if len(arr) > 2:
        return " ".join(arr[1:-1])

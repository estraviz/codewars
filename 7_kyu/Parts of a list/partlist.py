"""Parts of a list
"""


def partlist(arr):
    return [(' '.join(arr[0:index + 1]),
            ' '.join(arr[index+1:])) for index in range(len(arr) - 1)]

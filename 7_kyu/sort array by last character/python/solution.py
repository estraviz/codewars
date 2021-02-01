"""sort array by last character"""


def sort_me(arr):
    return sorted(arr, key=lambda x: str(x)[-1])

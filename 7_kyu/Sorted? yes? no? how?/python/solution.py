"""Sorted? yes? no? how?"""


def is_sorted_and_how(arr):
    return "yes, ascending" if is_sorted(arr, False) else "yes, descending" if is_sorted(arr, True) else "no"


def is_sorted(arr, reverse):
    return sorted(arr, reverse=reverse) == arr

"""All Star Code Challenge #22"""


def to_time(seconds):
    return f'{(h := seconds // 3600)} hour(s) and {(seconds - 3600 * h) // 60} minute(s)'

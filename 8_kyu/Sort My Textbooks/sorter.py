"""
Sort My Textbooks
"""


def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)

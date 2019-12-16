"""
Numbers to Letters
"""

from string import ascii_lowercase


def switcher(arr):
    punct = {'27': '!', '28': '?', '29': ' '}
    letters = ascii_lowercase[::-1]
    output = ''
    for num in arr:
        if num in punct:
            output += punct.get(num)
        else:
            output += letters[int(num) - 1]
    return output

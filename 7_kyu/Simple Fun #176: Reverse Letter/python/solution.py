"""Simple Fun #176: Reverse Letter"""

import re


def reverse_letter(string):
    return re.sub('[^a-zA-Z]', '', string)[::-1]

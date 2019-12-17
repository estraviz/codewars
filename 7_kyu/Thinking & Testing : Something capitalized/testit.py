"""
Thinking & Testing : Something capitalized
"""


def youtestit(s):
    return ' '.join(letter[::-1].title()[::-1] for letter in s.split())

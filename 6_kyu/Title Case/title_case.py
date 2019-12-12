"""
Title Case
"""


def title_case(title, minor_words=''):
    minor_words = '' if minor_words is None else minor_words.lower().split()
    return ' '.join(word if word in minor_words else word.capitalize()
                    for word in title.capitalize().split())

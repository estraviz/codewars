"""
Vowel remover (python 3.x version)
"""


def shortcut(s):
    return s.translate(s.maketrans('', '', 'aeiou'))

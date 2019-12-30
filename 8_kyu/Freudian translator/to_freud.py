"""
Freudian translator
"""


def to_freud(sentence):
    return ' '.join('sex' for word in sentence.split())

"""Arrh, grabscrab!"""

from collections import Counter


def grabscrab(word, possible_words):
    counter = Counter(word)
    return [p_w for p_w in possible_words if counter == Counter(p_w)]

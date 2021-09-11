"""Sort Arrays (Ignoring Case)"""


def sortme(words):
    return sorted(words, key=lambda x: x.lower())

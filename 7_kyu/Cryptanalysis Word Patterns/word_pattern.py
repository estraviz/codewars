"""Cryptanalysis Word Patterns
"""


def word_pattern(word):
    chars = dict()
    pattern = ""
    for c in word.lower():
        if not chars:
            chars[c] = 0
            pattern = "0"
        else:
            if c not in chars:
                chars[c] = max(chars.values()) + 1
            pattern = ".".join([pattern, str(chars.get(c))])
    return pattern

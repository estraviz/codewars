"""Simple Pig Latin
"""


def pig_it(txt):
    return " ".join(word if not word.isalpha() else
                    "".join([word[1:], word[0], 'ay']) for word in txt.split())

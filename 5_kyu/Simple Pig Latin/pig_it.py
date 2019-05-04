"""Simple Pig Latin
"""
from string import punctuation


def pig_it(text):
    return " ".join(["".join([word[1:], word[0], 'ay'])
                    if word.strip(punctuation)
                    else "".join([word[1:], word[0]])
                    for word in text.split()])

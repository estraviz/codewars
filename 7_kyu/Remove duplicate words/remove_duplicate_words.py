"""
Remove duplicate words
"""


def gen(s):
    set_of_words = set()
    for word in s.split():
        if word not in set_of_words:
            set_of_words.add(word)
            yield word


def remove_duplicate_words(s):
    return ' '.join(list(gen(s)))

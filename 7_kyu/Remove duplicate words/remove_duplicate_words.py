"""
Remove duplicate words
"""


def remove_duplicate_words(s):
    unique_words = []
    for word in s.split():
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)

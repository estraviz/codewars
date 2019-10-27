"""
Remove duplicate words
"""


def remove_duplicate_words(s):
    words = s.split()
    unique_words = []
    for word in words:
        if word in unique_words:
            continue
        else:
            unique_words.append(word)
    return ' '.join(unique_words)

"""Find the vowels"""


def vowel_indices(word):
    return [i + 1 for i, c in enumerate(word.lower()) if c in "aeiouy"]

# Character Counter
from collections import Counter


def validate_word(word):
    return len(set(Counter(word.lower()).values())) == 1

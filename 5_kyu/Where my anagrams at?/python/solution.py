"""Where my anagrams at?"""


def anagrams(word, words):
    word_sorted = sorted(word)
    return [w for w in words if word_sorted == sorted(w)]

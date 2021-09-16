"""Format words into a sentence"""


def format_words(words):
    if not words or not (words := [word for word in words if word]):
        return ""
    if len(words) == 1:
        return words[0]
    return " and ".join([", ".join(word for word in words[:-1]), words[-1]])

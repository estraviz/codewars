"""
Reversed Words
"""


def reverse_words(str):
    return " ".join([word for word in str.split(" ")][::-1])

"""Your order, please
"""


def order(sentence):
    return " ".join(sorted(sentence.split(), key=sorted))

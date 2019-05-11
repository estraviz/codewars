"""Your order, please
"""
from collections import OrderedDict


def order(sentence):
    positions = [ch for ch in sentence if ch.isdigit()]
    tuples = dict((idx, wrd) for idx, wrd in zip(positions, sentence.split()))
    ordered = OrderedDict(sorted(tuples.items(), key=lambda x: x[0]))
    return " ".join(ordered.values())

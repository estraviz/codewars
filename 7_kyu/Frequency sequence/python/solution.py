# Frequency sequence
from collections import Counter


def freq_seq(s, sep):
    return sep.join(str(Counter(s)[c]) for c in s)

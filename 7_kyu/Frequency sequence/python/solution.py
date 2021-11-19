# Frequency sequence
from collections import Counter


def freq_seq(s, sep):
    count = Counter(s)
    return sep.join(str(count[c]) for c in s)

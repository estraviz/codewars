# Frequency sequence
from collections import Counter


def freq_seq(s, sep):
    count = Counter(s)
    return "".join(str(count[c]) + sep for c in s)[:-1]

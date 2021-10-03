"""String Letter Counting"""

from collections import Counter
from collections import OrderedDict


def string_letter_count(s):
    counts = Counter(filter(str.isalpha, s.lower()))
    ordered_counts = OrderedDict(sorted(counts.items()))
    return "".join(str(v) + k for k, v in ordered_counts.items())

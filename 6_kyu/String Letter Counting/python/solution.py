"""String Letter Counting"""

from collections import defaultdict
from collections import OrderedDict


def string_letter_count(s):
    counts = defaultdict(int)
    for c in s.lower():
        if c.isalpha():
            counts[c] += 1
    ordered_counts = OrderedDict(sorted(counts.items()))
    return "".join(str(v) + k for k, v in ordered_counts.items())

"""First non-repeating character"""

from collections import Counter


def first_non_repeating_letter(s):
    count = Counter(s.lower())
    non_rep = [k for k, v in count.items() if v == 1]
    if not non_rep:
        return ''
    else:
        min_ind = min(s.index(c if c in s else c.upper()) for c in non_rep)
        return s[min_ind]

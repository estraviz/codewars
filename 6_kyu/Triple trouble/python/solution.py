"""Triple trouble"""

from collections import Counter
from collections import defaultdict


def triple_double(num1, num2):
    dd = defaultdict(list)

    for d in (Counter(str(num1)), Counter(str(num2))):
        for key, value in d.items():
            dd[key].append(value)

    for v in dd.values():
        if len(v) == 2:
            fst, snd = v
            if fst >= 3 and snd >= 2:
                return 1
    return 0

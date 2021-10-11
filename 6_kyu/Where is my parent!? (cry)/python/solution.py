"""Where is my parent!?(cry)"""

from collections import Counter
import re


def find_children(dancing_brigade):
    mothers = sorted(re.findall('([A-Z])', dancing_brigade))
    counts = dict(sorted(Counter(dancing_brigade).items(), key=lambda i: i[0]))
    output = ""
    for mother in mothers:
        output += mother
        if mother.lower() in counts.keys():
            output += counts[mother.lower()] * mother.lower()
    return output

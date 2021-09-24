"""Prize Draw"""

from string import ascii_uppercase
from collections import defaultdict
import operator


def rank(st, we, n):
    if not st:
        return "No participants"

    names = st.split(',')

    if n > len(names):
        return "Not enough participants"

    winning_number = defaultdict(str)

    for name, weight in zip(names, we):
        som = (
            len(name) + sum(
                ascii_uppercase.index(letter.upper()) + 1 for letter in name
                )
            )
        winning_number[name] = som * weight

    return sorted(
        sorted(
            winning_number.items(), key=operator.itemgetter(0)
        ), key=operator.itemgetter(1), reverse=True
    )[n - 1][0]

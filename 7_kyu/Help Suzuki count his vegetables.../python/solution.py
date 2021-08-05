"""Help Suzuki count his vegetables..."""

from collections import Counter
from operator import itemgetter


def count_vegetables(string):
    vegetables = [
        "cabbage", "carrot", "celery", "cucumber", "mushroom", "onion",
        "pepper", "potato", "tofu", "turnip"
    ]
    return sorted(
        [
            (value, key) for key, value in Counter(string.split()).items()
            if key in vegetables
        ], key=itemgetter(0, 1), reverse=True
    )

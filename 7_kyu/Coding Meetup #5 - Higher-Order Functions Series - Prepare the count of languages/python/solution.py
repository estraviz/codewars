# Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages
from collections import defaultdict


def count_languages(lst):
    result = defaultdict(int)
    for obj in lst:
        for k, v in obj.items():
            if k == 'language':
                result[v] += 1
    return result

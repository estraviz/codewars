"""Building Strings From a Hash"""


def solution(pairs):
    return ','.join(sorted(f"{k} = {v}" for k, v in pairs.items()))

# Rearrange Number to Get its Maximum
from itertools import permutations


def max_redigit(num):
    if 100 <= num <= 999:
        return max(
            [int(''.join(x)) for x in permutations(str(num), len(str(num)))]
            )

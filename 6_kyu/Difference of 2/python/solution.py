"""Difference of 2"""


def twos_difference(lst):
    result = []
    for i, num in enumerate(lst):
        j = i + 1
        while j < len(lst):
            if abs(num - lst[j]) == 2:
                result.append(tuple(sorted([num, lst[j]])))
            j += 1
    return sorted(result)

# Consecutive Differences
def differences(lst):
    return lst[0] if len(lst) == 1 else differences(
        [abs(x-y) for x, y in zip(lst, lst[1:])]
    )

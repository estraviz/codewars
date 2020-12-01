"""Balanced n (Special ns Series #1 )
"""


def balanced_num(n):
    return (
        "Balanced"
        if sum(
            int(x) for x in str(n)[: len(str(n)) // 2 + (0 if len(str(n)) % 2 else -1)]
        )
        == sum(int(x) for x in str(n)[len(str(n)) // 2 + 1 :])
        else "Not Balanced"
    )

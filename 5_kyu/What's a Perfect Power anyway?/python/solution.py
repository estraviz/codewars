"""What's a Perfect Power anyway?"""


def isPP(n):
    for i in range(2, n):
        k = round(n ** (1/i), 0)
        if k ** i == n:
            return [k, i]

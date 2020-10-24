"""Check that the situation is correct
"""

from collections import Counter


def is_it_possible(field):
    counter = Counter([chr for chr in field])
    cnt_X, cnt_0 = counter["X"], counter["0"]

    if cnt_X > cnt_0 + 1 or cnt_0 > cnt_X:
        return False

    rows = [field[i : i + 3] for i in range(0, 9, 3)]
    columns = [field[i] + field[i + 3] + field[i + 6] for i in range(3)]

    all_X = (
        validate_segment(rows, "X")
        + validate_segment(columns, "X")
        + is_in_diagonals("X", field)
    )
    all_0 = (
        validate_segment(rows, "0")
        + validate_segment(columns, "0")
        + is_in_diagonals("0", field)
    )

    if (
        any([all_X, all_0]) >= 2
        or (all_X > all_0 and cnt_X == cnt_0 and cnt_X + cnt_0 < 9)
        or (all_X > all_0 and cnt_X < cnt_0)
        or (all_0 > all_X and cnt_X > cnt_0)
        or all([all_X, all_0]) >= 1
    ):
        return False

    return True


def validate_segment(segments, item):
    return sum(1 for s in segments if item in s and len(set(s)) == 1)


def is_in_diagonals(chr, field):
    cnt = 0
    if chr in field[0] and len(set([field[0], field[4], field[8]])) == 1:
        cnt += 1
    if chr in field[2] and len(set([field[2], field[4], field[6]])) == 1:
        cnt += 1
    return cnt

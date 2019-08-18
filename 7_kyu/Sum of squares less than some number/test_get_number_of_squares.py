from get_number_of_squares import get_number_of_squares

test_cases = (
    (1, 0),
    (2, 1),
    (5, 1),
    (6, 2),
    (15, 3),
)


def test_get_number_of_squares():
    for t in test_cases:
        inp, exp = t
        assert get_number_of_squares(inp) == exp

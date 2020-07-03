from starting_mark import starting_mark


def test_basic():
    assert starting_mark(1.52) == 9.45
    assert starting_mark(1.83) == 10.67
    assert starting_mark(1.22) == 8.27
    assert starting_mark(2.13) == 11.85
    assert starting_mark(1.75) == 10.36

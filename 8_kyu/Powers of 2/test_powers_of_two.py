from powers_of_two import powers_of_two


def test_powers_of_two():
    assert powers_of_two(0) == [1]
    assert powers_of_two(1) == [1, 2]
    assert powers_of_two(4) == [1, 2, 4, 8, 16]

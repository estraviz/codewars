from largest_power import largest_power


def test_small_cases():
    assert largest_power(2) == 0
    assert largest_power(3) == 0
    assert largest_power(4) == 1
    assert largest_power(5) == 1
    assert largest_power(7) == 1


def test_large_cases():
    assert largest_power(81) == 3
    assert largest_power(82) == 4
    assert largest_power(59049) == 9
    assert largest_power(59050) == 10
    assert largest_power(123456789) == 16
    assert largest_power(987654321) == 18


def test_edge_case():
    assert largest_power(1) == -1

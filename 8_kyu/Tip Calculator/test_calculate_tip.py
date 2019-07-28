from calculate_tip import calculate_tip


def test_calculate_tip():
    assert calculate_tip(30, "poor") == 2
    assert calculate_tip(20, "Excellent") == 4
    assert calculate_tip(20, "hi") == 'Rating not recognised'
    assert calculate_tip(107.65, "GReat") == 17
    assert calculate_tip(20, "great!") == 'Rating not recognised'

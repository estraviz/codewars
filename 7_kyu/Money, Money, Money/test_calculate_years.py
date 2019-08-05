from calculate_years import calculate_years


def test_calculate_years():
    assert calculate_years(1000, 0.05, 0.18, 1100) == 3
    assert calculate_years(1000, 0.01625, 0.18, 1200) == 14
    assert calculate_years(1000, 0.05, 0.18, 1000) == 0

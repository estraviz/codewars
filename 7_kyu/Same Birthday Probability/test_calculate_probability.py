from calculate_probability import calculate_probability


def test_calculate_probability():
    assert calculate_probability(5) == 0.03
    assert calculate_probability(15) == 0.25
    assert calculate_probability(1) == 0
    assert calculate_probability(365) == 1
    assert calculate_probability(366) == 1

from no_boring_zeros import no_boring_zeros


def test_no_boring_zeros():
    assert no_boring_zeros(1450) == 145
    assert no_boring_zeros(960000) == 96
    assert no_boring_zeros(1050) == 105
    assert no_boring_zeros(-1050) == -105
    assert no_boring_zeros(0) == 0
    assert no_boring_zeros(2016) == 2016

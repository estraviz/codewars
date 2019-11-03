from unlucky_days import unlucky_days


def test_unlucky_days():
    assert unlucky_days(2015) == 3
    assert unlucky_days(1986) == 1
    assert unlucky_days(1634) == 2
    assert unlucky_days(2873) == 2
    assert unlucky_days(1586) == 1

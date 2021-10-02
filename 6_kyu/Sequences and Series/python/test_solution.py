from solution import get_score


def test_basic():
    assert get_score(1) == 50
    assert get_score(2) == 150
    assert get_score(3) == 300
    assert get_score(4) == 500
    assert get_score(5) == 750

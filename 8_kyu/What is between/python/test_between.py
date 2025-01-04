from between import between


def test_between():
    assert between(1, 4) == [1, 2, 3, 4]
    assert between(5, 500) == list(range(5, 500 + 1))
    assert between(-10, 10) == list(range(-10, 10 + 1))
    assert between(-2, 2) == list(range(-2, 2 + 1))

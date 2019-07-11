from enough import enough


def test_enough():
    assert enough(10, 5, 5) == 0
    assert enough(100, 60, 50) == 10
    assert enough(20, 5, 5) == 0

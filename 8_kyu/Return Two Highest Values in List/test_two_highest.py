from two_highest import two_highest


def test_two_highest():
    assert two_highest([]) == []
    assert two_highest("cool") is False
    assert two_highest([15, 20, 20, 17]) == [20, 17]

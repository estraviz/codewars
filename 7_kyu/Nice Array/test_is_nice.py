from is_nice import is_nice


def test_is_nice():
    assert is_nice([2, 10, 9, 3]) is True
    assert is_nice([3, 4, 5, 7]) is False

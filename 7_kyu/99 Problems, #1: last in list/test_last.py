from last import last


def test_last():
    assert last([1, 2, 3]) == 3
    assert last([]) is None
    assert last([2, 1, 0]) == 0
    assert last(["a", "b", ""]) == ""

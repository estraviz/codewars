from solution import solve


def test_solve():
    assert solve("abc") is True
    assert solve("abd") is False
    assert solve("dabc") is True
    assert solve("abbc") is False

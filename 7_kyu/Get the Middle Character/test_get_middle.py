from get_middle import get_middle


def test_get_middle():
    assert get_middle("test") == "es"
    assert get_middle("testing") == "t"
    assert get_middle("middle") == "dd"
    assert get_middle("A") == "A"
    assert get_middle("of") == "of"

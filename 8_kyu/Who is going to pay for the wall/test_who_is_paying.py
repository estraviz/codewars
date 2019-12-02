from who_is_paying import who_is_paying


def test_who_is_paying():
    assert who_is_paying("Mexico") == ["Mexico", "Me"]
    assert who_is_paying("Melania") == ["Melania", "Me"]
    assert who_is_paying("Melissa") == ["Melissa", "Me"]
    assert who_is_paying("Me") == ["Me"]
    assert who_is_paying("") == [""]
    assert who_is_paying("I") == ["I"]

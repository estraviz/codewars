from correct_tail import correct_tail


def test_correct_tail():
    assert correct_tail("Fox", "x") is True
    assert correct_tail("Rhino", "o") is True
    assert correct_tail("Meerkat", "t") is True
    assert correct_tail("Emu", "t") is False
    assert correct_tail("Badger", "s") is False
    assert correct_tail("Giraffe", "d") is False

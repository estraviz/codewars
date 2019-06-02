from capitals import capitals


def test_capitals():
    assert capitals('CodEWaRs') == [0, 3, 4, 6]
    assert capitals('cODewArS') == [1, 2, 5, 7]

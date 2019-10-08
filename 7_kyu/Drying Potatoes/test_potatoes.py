from potatoes import potatoes


def test_potatoes():
    assert potatoes(82, 127, 80) == 114
    assert potatoes(93, 129, 91) == 100

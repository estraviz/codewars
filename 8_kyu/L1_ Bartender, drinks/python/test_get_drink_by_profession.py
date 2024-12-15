from get_drink_by_profession import get_drink_by_profession


def test_basic():
    assert get_drink_by_profession("jabrOni") == "Patron Tequila"
    assert get_drink_by_profession(
        "scHOOl counselor") == "Anything with Alcohol"
    assert get_drink_by_profession("prOgramMer") == "Hipster Craft Beer"
    assert get_drink_by_profession("bike ganG member") == "Moonshine"
    assert get_drink_by_profession("poLiTiCian") == "Your tax dollars"
    assert get_drink_by_profession("rapper") == "Cristal"
    assert get_drink_by_profession("pundit") == "Beer"
    assert get_drink_by_profession("Pug") == "Beer"

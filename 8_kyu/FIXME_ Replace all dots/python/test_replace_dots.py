from replace_dots import replace_dots


def test_replace_dots():
    assert replace_dots("") == ""
    assert replace_dots("no dots") == "no dots"
    assert replace_dots("one.two.three") == "one-two-three"
    assert replace_dots("........") == "--------"

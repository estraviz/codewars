from square_color import square_color


def test_square_color():
    assert square_color("a", 8) == "white"
    assert square_color("b", 2) == "black"
    assert square_color("f", 5) == "white"

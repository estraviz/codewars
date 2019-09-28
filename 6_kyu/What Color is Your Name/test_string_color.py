from string_color import string_color


def test_string_color():
    assert string_color("Jack") == "79CAE5"
    assert string_color("John Doe") == "C70033"
    assert string_color("CodeWars") == "182892"
    assert string_color("X") is None

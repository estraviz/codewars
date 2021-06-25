from solution import highest_value


def test_should_handle_alphanumeric_strings():
    assert highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567") == \
        "KkLlMmNnOoPp4567"
    assert highest_value("ABcd", "0123") == "ABcd"


def test_should_handle_non_alphanumeric_ascii():
    assert highest_value("!\"?$%^&*()", "{}[]@~'#:;") == "{}[]@~'#:;"


def test_should_handle_ties():
    assert highest_value("ABCD", "DCBA") == "ABCD"

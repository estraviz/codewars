from to_freud import to_freud


def test_to_freud():
    assert to_freud("test") == "sex"
    assert to_freud("sexy sex") == "sex sex"
    assert to_freud("This is a test") == "sex sex sex sex"
    assert to_freud("This is a longer test") == "sex sex sex sex sex"
    assert to_freud(
        "You're becoming a true freudian expert") == "sex sex sex sex sex sex"

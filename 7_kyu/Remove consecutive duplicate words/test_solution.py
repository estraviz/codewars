from solution import remove_consecutive_duplicates


def test_remove_consecutive_duplicates():
    s = (
        "alpha beta beta gamma gamma gamma delta alpha beta beta gamma "
        + "gamma gamma delta"
    )
    s_out = "alpha beta gamma delta alpha beta gamma delta"
    assert remove_consecutive_duplicates(s) == s_out

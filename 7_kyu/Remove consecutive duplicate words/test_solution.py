import pytest
from solution import remove_consecutive_duplicates


@pytest.mark.parametrize(
    "s, s_out",
    [
        ("", ""),
        (
            "alpha beta beta gamma gamma gamma delta alpha beta beta "
            + "gamma gamma gamma delta",
            "alpha beta gamma delta alpha beta gamma delta",
        ),
        ("iIi IiI", "iIi IiI"),
        ("aa a aa a aa", "aa a aa a aa"),
        ("this his is is sih siht", "this his is sih siht"),
        ("don't don t do not dont", "don't don t do not dont"),
    ],
)
def test_remove_consecutive_duplicates(s, s_out):
    assert remove_consecutive_duplicates(s) == s_out

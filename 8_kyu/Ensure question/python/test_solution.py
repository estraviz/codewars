import pytest

from solution import ensure_question


data = [
    ("", "?"),
    ("Yes", "Yes?"),
    ("No?", "No?"),
]


@pytest.mark.parametrize(
    "s, result", data
)
def test_ensure_question(s, result):
    assert ensure_question(s) == result

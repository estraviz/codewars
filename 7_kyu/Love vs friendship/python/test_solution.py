import pytest

from solution import words_to_marks


data = [
    ('attitude', 100),
    ('friends', 75),
    ('family', 66),
    ('selfness', 99),
    ('knowledge', 96),
]


@pytest.mark.parametrize(
    "s, expected", data
)
def test_words_to_marks(s, expected):
    assert words_to_marks(s) == expected

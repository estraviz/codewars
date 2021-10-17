import pytest

from solution import to_underscore


tests = [
    ("TestController", "test_controller"),
    ("MoviesAndBooks", "movies_and_books"),
    ("App7Test", "app7_test"),
    (1, "1"),
]


@pytest.mark.parametrize(
    "string, expected", tests
)
def test_to_underscore(string, expected):
    assert to_underscore(string) == expected

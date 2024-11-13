import pytest

from main import string_to_array


tests = [
    ("Robin Singh", ["Robin", "Singh"]),
    ("CodeWars", ["CodeWars"]),
    (
        "I love arrays they are my favorite",
        [
            "I", "love", "arrays", "they", "are", "my", "favorite"
        ]
    ),
    ("1 2 3", ["1", "2", "3"]),
    ("", [""]),
]


@pytest.mark.parametrize(
    "s, expected", tests
)
def test_string_to_array(s, expected):
    assert string_to_array(s) == expected

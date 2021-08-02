import pytest

from solution import my_languages


tests = [
    ({"Java": 10, "Ruby": 80, "Python": 65}, ["Ruby", "Python"]),
    ({"Hindi": 60, "Dutch": 93, "Greek": 71}, ["Dutch", "Greek", "Hindi"]),
    ({"C++": 50, "ASM": 10, "Haskell": 20}, []),
]


@pytest.mark.parametrize(
    "results, expected", tests
)
def test_my_languages(results, expected):
    assert my_languages(results) == expected

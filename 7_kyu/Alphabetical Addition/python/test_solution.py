import pytest

from solution import add_letters


tests = [
    (['a', 'b', 'c'], 'f'),
    (['z'], 'z'),
    (['a', 'b'], 'c'),
    (['c'], 'c'),
    (['z', 'a'], 'a'),
    (['y', 'c', 'b'], 'd'),
    ([], 'z')
]


@pytest.mark.parametrize(
    "letters, expected", tests
)
def test_fixed_tests(letters, expected):
    assert add_letters(*letters) == expected

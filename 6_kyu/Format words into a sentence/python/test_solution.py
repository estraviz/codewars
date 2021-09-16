import pytest

from solution import format_words


tests = [
    (['one', 'two', 'three', 'four'], 'one, two, three and four'),
    (['one'], 'one'),
    (['one', '', 'three'], 'one and three'),
    (['', '', 'three'], 'three'),
    (['one', 'two', ''], 'one and two'),
    ([], ''),
    (None, ''),
    ([''], ''),
]


@pytest.mark.parametrize(
    "words, expected", tests
)
def test_format_words(words, expected):
    assert format_words(words) == expected

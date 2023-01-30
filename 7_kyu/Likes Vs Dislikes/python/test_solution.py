import pytest

from solution import like_or_dislike


tests = [
    (['Dislike'], 'Dislike'),
    (['Like', 'Like'], 'Nothing'),
    (['Dislike', 'Dislike'], 'Nothing'),
    (['Like', 'Like', 'Like'], 'Like'),
    (['Like', 'Dislike'], 'Dislike'),
    (['Dislike', 'Like'], 'Like'),
    (['Like', 'Dislike', 'Dislike'], 'Nothing'),
    (['Dislike', 'Like', 'Dislike'], 'Dislike'),
    (['Like', 'Like', 'Dislike', 'Like', 'Like', 'Like', 'Like', 'Dislike'],
     'Dislike'),
    ([], 'Nothing')
]


@pytest.mark.parametrize(
    "data, expected", tests
)
def test_basic_tests(data, expected):
    assert like_or_dislike(data) == expected

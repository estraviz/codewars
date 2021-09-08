import pytest

from solution import kebabize


tests = [
    ('myCamelCasedString', 'my-camel-cased-string'),
    ('myCamelHas3Humps', 'my-camel-has-humps'),
    ('SOS', 's-o-s'),
    ('42', ''),
    ('CodeWars', 'code-wars'),
]


@pytest.mark.parametrize(
    "string, expected", tests
)
def test_kebabize(string, expected):
    assert kebabize(string) == expected

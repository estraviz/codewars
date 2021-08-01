import pytest

from solution import scramble


tests = [
    ('rkqodlw', 'world', True),
    ('cedewaraaossoqqyt', 'codewars', True),
    ('katas', 'steak', False),
    ('scriptjavx', 'javascript', False),
    ('scriptingjava', 'javascript', True),
    ('scriptsjava', 'javascripts', True),
    ('javscripts', 'javascript', False),
    ('aabbcamaomsccdd', 'commas', True),
    ('commas', 'commas', True),
    ('sammoc', 'commas', True),
]


@pytest.mark.parametrize(
    "s1, s2, expected", tests
)
def test_scramble(s1, s2, expected):
    assert scramble(s1, s2) == expected

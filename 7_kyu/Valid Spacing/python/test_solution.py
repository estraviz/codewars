import pytest

from solution import valid_spacing


sample_tests = [
    ('Hello world', True),
    (' Hello world', False),
    ('Hello  world ', False),
    ('Hello', True),
    ('Helloworld', True),
]


@pytest.mark.parametrize("s, expected", sample_tests)
def test_sample_valid_spacing(s, expected):
    assert valid_spacing(s) == expected


basic_tests = [
    ('codewars ', False),
    (' code wars  ', False),
    ('c o d e w a r s', True),
    ('cod  ewars', False),
    ('codewars', True),
]


@pytest.mark.parametrize("s, expected", basic_tests)
def test_basic_valid_spacing(s, expected):
    assert valid_spacing(s) == expected


edge_tests = [
    (' ', False),
    ('', True),
    ('   ', False),
]


@pytest.mark.parametrize("s, expected", edge_tests)
def test_edge_valid_spacing(s, expected):
    assert valid_spacing(s) == expected

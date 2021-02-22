import pytest

from solution import luck_check


data = [
    ('683179', True),
    ('683000', False),
    ('5555', True),
    ('003111', True),
    ('543970707', False),
    ('439924', False),
    ('943294329932', False),
    ('000000', True),
    ('454319', True),
    ('1233499943', False),
    ('935336', False),
]


@pytest.mark.parametrize(
    "string, result", data
)
def test_numeric_string(string, result):
    assert luck_check(string) is result


data_err = [
    ('6F43E8'),
    ('6F43E8'),
    ('1234 '),
    ('124-21'),
]


@pytest.mark.parametrize(
    "string", data_err
)
def test_non_numeric_string_should_raise(string):
    with pytest.raises(ValueError):
        luck_check(string)

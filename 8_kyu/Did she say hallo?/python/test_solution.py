import pytest

from solution import validate_hello

data = [
    ('hello', True),
    ('ciao bella!', True),
    ('salut', True),
    ('hallo, salut', True),
    ('hombre! Hola!', True),
    ('Hallo, wie geht\'s dir?', True),
    ('AHOJ!', True),
    ('czesc', True),
    ('meh', False),
    ('Ahoj', True),
]


@pytest.mark.parametrize(
    "greetings, result", data
)
def test_validate_hello(greetings, result):
    assert validate_hello(greetings) == result

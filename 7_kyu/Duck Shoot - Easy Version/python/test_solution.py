import pytest

from solution import duck_shoot


tests = [
    (4, 0.64, '|~~2~~~22~2~~22~2~~~~2~~~|', '|~~X~~~X2~2~~22~2~~~~2~~~|'),
    (9, 0.22, '|~~~~~~~2~2~~~|', '|~~~~~~~X~2~~~|'),
    (6, 0.41, '|~~~~~22~2~~~~~|', '|~~~~~XX~2~~~~~|'),
    (8, 0.05, '|2~~~~|', '|2~~~~|'),
    (8, 0.92, '|~~~~2~2~~~~~22~~2~~~~2~~~2|', '|~~~~X~X~~~~~XX~~X~~~~X~~~X|'),
]


@pytest.mark.parametrize(
    "ammo, aim, ducks, expected", tests
)
def test_duck_shoot(ammo, aim, ducks, expected):
    assert duck_shoot(ammo, aim, ducks) == expected

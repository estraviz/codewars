import pytest

from solution import borrow


data = [
    ('WhAt! FiCK! DaMn CAke?', 'whatfickdamncake'),
    ('THE big PeOpLE Here!!', 'thebigpeoplehere'),
    ('i AM a TINY BoY!!', 'iamatinyboy'),
]


@pytest.mark.parametrize(
    "s, result", data
)
def test_borrow(s, result):
    assert borrow(s) == result

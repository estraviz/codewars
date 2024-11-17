import pytest
from solution import greet


data = [
    ('Daniel', 'Daniel', 'Hello boss'),
    ('Greg', 'Daniel', 'Hello guest'),
]


@pytest.mark.parametrize("name, owner, result", data)
def test_domain_name(name, owner, result):
    assert greet(name, owner) == result

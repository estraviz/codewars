import pytest

from solution import solution


data = [
    ("helloWorld", "hello World"),
    ("camelCase", "camel Case"),
    ("breakCamelCase", "break Camel Case"),
]


@pytest.mark.parametrize("s, result", data)
def test_solution(s, result):
    assert solution(s) == result

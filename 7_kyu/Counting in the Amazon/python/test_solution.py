import pytest

from solution import count_arara


data = [
    (1, "anane"),
    (2, "adak"),
    (3, "adak anane"),
    (9, "adak adak adak adak anane"),
]


@pytest.mark.parametrize("n, result", data)
def test_count_arara(n, result):
    assert count_arara(n) == result

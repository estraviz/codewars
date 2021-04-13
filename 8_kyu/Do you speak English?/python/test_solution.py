import pytest

from solution import sp_eng


data = [
    ("english", True),
    ("egnlish", False),
    ("1234egn lish", False),
    ("1234english k", True),
    ("English", True),
    ("eNgliSh", True),
    ("1234#$%%eNglish k9", True),
    ("EGNlihs", False),
    ("1234englihs**", False),
]


@pytest.mark.parametrize(
    "sentence, result", data
)
def test_example_test_case(sentence, result):
    assert sp_eng(sentence) == result


def test_edge_test_case():
    assert sp_eng("") is False

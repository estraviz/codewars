import pytest

from solution import spacey


data = [
    (
        ["kevin", "has", "no", "space"],
        ["kevin", "kevinhas", "kevinhasno", "kevinhasnospace"],
    ),
    (
        ["this", "cheese", "has", "no", "holes"],
        [
            "this",
            "thischeese",
            "thischeesehas",
            "thischeesehasno",
            "thischeesehasnoholes",
        ],
    ),
]


@pytest.mark.parametrize("array, result", data)
def test_spacey(array, result):
    assert spacey(array) == result

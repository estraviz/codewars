import pytest

from solution import are_you_playing_banjo

data = [
    ("Martin", "Martin does not play banjo"),
    ("Rikke", "Rikke plays banjo"),
    ("bravo", "bravo does not play banjo"),
    ("rolf", "rolf plays banjo"),
]

@pytest.mark.parametrize("name, result", data)
def test_are_you_playing_banjo(name, result):
    assert are_you_playing_banjo(name) == result

import pytest

from solution import simple_transposition


tests = [
    ("Sample text", "Sml etapetx"),
    ("Simple transposition", "Sml rnpstoipetasoiin"),
    ("All that glitters is not gold", "Alta ltesi o odl htgitr sntgl"),
    ("The better part of valor is discretion", "Tebte ato ao sdsrtoh etrpr fvlri icein"),
    ("Conscience does make cowards of us all", "Cncec osmk oad fu losinede aecwrso sal"),
    ("Imagination is more important than knowledge", "Iaiaini oeipratta nwegmgnto smr motn hnkolde"),
]


@pytest.mark.parametrize(
    "text, expected", tests
)
def test_simple_transposition(text, expected):
    assert simple_transposition(text) == expected

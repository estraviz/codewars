import pytest

from solution import dna_to_rna

data = [
    ("GCAT", "GCAU"),
    ("TTTT", "UUUU"),
    ("GCAT", "GCAU"),
    ("GACCGCCGCC", "GACCGCCGCC"),
]

@pytest.mark.parametrize(
    "dna, expected", data
)
def test_dna_to_rna(dna, expected):
    assert dna_to_rna(dna) == expected

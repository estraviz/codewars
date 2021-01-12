import pytest

from solution import split_and_merge


data = [
    ("My name is John", " ", "M y n a m e i s J o h n"),
    ("My name is John", "-", "M-y n-a-m-e i-s J-o-h-n"),
    ("Hello World!", ".", "H.e.l.l.o W.o.r.l.d.!"),
    ("Hello World!", ",", "H,e,l,l,o W,o,r,l,d,!"),
]


@pytest.mark.parametrize("string_, separator, result", data)
def test_split_and_merge(string_, separator, result):
    assert split_and_merge(string_, separator) == result

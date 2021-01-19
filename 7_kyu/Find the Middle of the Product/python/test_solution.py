import pytest

from solution import find_middle


data = [
    ("s7d8jd9", 0),
    ("58jd9fgh/fgh6s.,sdf", 16),
    ("s7d8jd9dfg4d", 1),
    ("s7d8j", 56),
    ("asd.fasd.gasdfgsdfgh-sdfghsdfg/asdfga=sdfg", -1),
    ("44555", 0),
    (None, -1),
    ([1, 2, 3, 4, 5, 6], -1),
    (["a", "b", "c"], -1),
    ("5d8jd9fgh/fgh6s.,sdf8sdf9sdf98 3  0", 0),
    ("         ", -1),
    ("e^6*9=#asdfd7-4", 51),
    ("s7d8jd9qwertqwrt v654ed1frg651", 4),
    ("58", 40),
    ("s7d1548jd9dfg4d", 3),
    ("s7d54sd6f48j", 8),
    ("asd.fasd.gasdfgsdf1gh-sdfghsdfg/asdfga=sdfg", 1),
    ("44145s555", 0),
    ("sdf496as4df6", 18),
    (4554, -1),
    ("asdf544684868", 8),
    ("5d8jd9fgh/fgh64f4f4f00s.,sdf8sdf9sdf98", 0),
    ("    s2     ", 2),
    ("e^6*9=#as5ddfd7-4", 56),
    ("s7d8j987d9", 40),
    ("58jd9636fgh/fgh6s.,sdf", 32),
    ("s7d8j546sdfd9dfg4d", 19),
    ("s7d8sdfs165d41fj", 72),
    ("asd.fasd.ga654sdfgsdfgh-sdfghsdfg/asdfga=sdfg", 2),
    ("4456846955", 36),
    (56465462165484, -1),
    (["a", 1, 2, 3, 4, 5, 6], -1),
    (["a", "b", "c", "sfd"], -1),
    ("5d8jd9fgh/fgh6s.,6574ssdf8sdf9sdf98 3", 5),
    ("     99    ", 81),
    ("e^6*9984=#asdfd7-4", 54),
    ("s7d8js599d9", 41),
    ("58jd9fgh654d/fgh6s.,sdf", 92),
    ("s7d8jd654sdf9dfg4d", 19),
    ("s7asdf68545fd8j", 88),
    ("asd.f855dasd.gasdfgsdfgh-sdfghsdfg/asdfga=sdfg", 0),
    ("445 2 2 55", 0),
    ("nu11", 1),
    ("[1,2,3,4,5,6]", 2),
    ("[a, b, c, 4, 3]", 12),
    ("5d8jd9fgh/fgh6s.,sdf8s5sdf9sdf98 3 ", 6),
    ("     /./\\    ", -1),
    ("e^6*9=52d#asdfd7-4", 1),
    ("s7564d56d56d8jd9", 32),
    ("58jd9fgh/fg97987d9fgh6s.,sdf", 5),
]


@pytest.mark.parametrize("string, result", data)
def test_find_middle(string, result):
    assert find_middle(string) == result

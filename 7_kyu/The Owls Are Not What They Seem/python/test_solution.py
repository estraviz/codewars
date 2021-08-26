import pytest

from solution import owl_pic


tests = [
   ('xwe', "XW''0v0''WX"),
   ("kuawd6r8q27y87t93r76352475437", "UAW8Y8T''0v0''T8Y8WAU"),
   ("t6ggggggggWw", "TWW''0v0''WWT"),
   ('xweWXo', "XWWXO''0v0''OXWWX"),
]


@pytest.mark.parametrize(
    "text, expected", tests
)
def test_owl_pic(text, expected):
    assert owl_pic(text) == expected

import pytest
import datetime

from solution import get_villain_name


@pytest.mark.parametrize(
    "date, name",
    [
        ("1/1/2000", "The Evil Pickle"),
        ("2/2/2000", "The Vile Hood Ornament"),
        ("2/12/2000", "The Awkward Hood Ornament"),
        ("18/11/2000", "The Terrifying Teaspoon"),
    ],
)
def test_example_tests(date, name):
    format_str = "%d/%m/%Y"
    get_villain_name(datetime.datetime.strptime(date, format_str)) == name

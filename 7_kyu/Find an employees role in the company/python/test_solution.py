import pytest

from solution import find_employees_role


tests_equals = [
    ("Dipper Pines", "Does not work here!"),
    ("Morty Smith", "Truck Driver"),
    ("Anna Bell", "Admin"),
    ("Anna", "Does not work here!"),
    ("Bell Anna", "Does not work here!"),
    ("Jewel Bell", "Receptionist"),
    ("Bell Jewel", "Does not work here!"),
]


@pytest.mark.parametrize(
    "name, expected", tests_equals
)
def test_find_employees_role_is_ok(name, expected):
    assert find_employees_role(name) == expected


tests_not_equals = [
    ("Anna Bell", "Sales Assistant"),
    ("Ollie Hepburn", "Warehouse Manager"),
    ("Morty Smith", "Warehouse Picker"),
]


@pytest.mark.xfail
@pytest.mark.parametrize(
    "name, expected", tests_equals
)
def test_find_employees_role_not_ok(name, expected):
    assert find_employees_role(name) == expected

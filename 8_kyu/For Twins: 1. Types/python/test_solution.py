from solution import type_validation


def test_type_validation():
    assert type_validation(42, "int") is True
    assert type_validation("42", "int") is False

from create_phone_number import create_phone_number


def test_create_phone_number():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert create_phone_number(arr) == "(123) 456-7890"

    arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert create_phone_number(arr) == "(111) 111-1111"

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert create_phone_number(arr) == "(123) 456-7890"

    arr = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]
    assert create_phone_number(arr) == "(023) 056-0890"

    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert create_phone_number(arr) == "(000) 000-0000"

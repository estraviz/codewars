from last import last


def test_last_item_of_an_array_of_numbers():
    assert last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10


def test_last_argument_numbers():
    assert last(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 10


def test_last_item_of_an_array_of_strings():
    assert last(list("abckxyz")) == "z"


def test_last_char_of_a_string():
    assert last("abckxyz") == "z"


def test_last_argument_chars():
    assert last("a", "b", "c", "z") == "z"


def test_last_item_of_only_argument():
    assert last(5) == 5

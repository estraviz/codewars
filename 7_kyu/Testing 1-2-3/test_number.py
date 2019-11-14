from number import number


def test_should_handle_empty_arrays():
    assert number([]) == []


def test_should_handle_normal_cases():
    assert number(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]


def test_should_handle_all_empty_lines():
    assert number(["", "", "", "", ""]) == ["1: ", "2: ", "3: ", "4: ", "5: "]


def test_should_handle_some_empty_lines():
    assert number(["", "b", "", "",
                   ""]) == ["1: ", "2: b", "3: ", "4: ", "5: "]

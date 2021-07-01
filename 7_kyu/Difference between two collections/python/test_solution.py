from solution import diff


def test_should_return_empty_for_the_same_content():
    assert diff(['a', 'b'], ['a', 'b']) == []


def test_should_return_A_if_B_is_empty():
    a = ['a', 'b']
    b = []
    assert diff(a, b) == a


def test_should_return_B_if_A_is_empty():
    a = []
    b = ['a', 'b']
    assert diff(a, b) == b


def test_should_return_empty_for_the_empty_content():
    assert diff([], []) == []


def test_should_return_the_last_character():
    a = ['a', 'b', 'z']
    b = ['a', 'b']
    assert diff(a, b) == ['z']


def test_should_return_the_sorted_characters():
    a = ['a', 'b', 'z', 'd', 'e', 'd']
    b = ['a', 'b', 'j', 'j']
    assert diff(a, b) == ['d', 'e', 'j', 'z']

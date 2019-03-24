from unique_in_order import unique_in_order


def test_should_work_with_empty_array():
    assert unique_in_order('') == []


def test_should_work_with_one_element():
    assert unique_in_order('A') == ['A']


def test_should_reduce_duplicates():
    assert unique_in_order('AA') == ['A']
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    assert unique_in_order('AADD') == ['A', 'D']
    assert unique_in_order('AAD') == ['A', 'D']
    assert unique_in_order('ADD') == ['A', 'D']


def test_should_treat_lowercase_as_different_from_uppercase():
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']


def test_should_work_with_int_arrays():
    assert unique_in_order([1, 2, 3, 3]) == [1, 2, 3]


def test_should_work_with_char_arrays():
    assert unique_in_order(['a', 'b', 'b']) == ['a', 'b']

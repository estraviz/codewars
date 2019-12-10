from count import count


def test_should_give_empty_dictionary_if_string_is_empty():
    assert count('') == {}


def test_should_get_as_a_result_two_A_characters():
    assert count('aa') == {'a': 2}


def test_should_get_as_a_result_of_two_a_characters_and_two_b_characters():
    assert count('aabb') == {'a': 2, 'b': 2}


def test_should_show_that_the_result_order_does_not_matter():
    assert count('aabb') == {'b': 2, 'a': 2}

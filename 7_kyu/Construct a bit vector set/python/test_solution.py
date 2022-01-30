from solution import sort_by_bit


def test_should_return_0_if_empty_array_is_provided():
    assert sort_by_bit([]) == 0


def test_should_return_1_if_array_with_zero_is_provided():
    assert sort_by_bit([0]) == 1


def test_should_return_3_if_array_with_zero_and_1_is_provided():
    assert sort_by_bit([0, 1]) == 3


def test_should_return_3_if_array_with_zero_and_1_is_provided_order_shouldn_not_matter():
    assert sort_by_bit([1, 0]) == 3


def test_should_return_1073741825_if_array_with_30_and_0_provided():
    assert sort_by_bit([30, 0]) == 1073741825

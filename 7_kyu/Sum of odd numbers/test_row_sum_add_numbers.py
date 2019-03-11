from row_sum_add_numbers import row_sum_odd_numbers


def test_row_sum_add_numbers():
    assert row_sum_odd_numbers(1) == 1
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(13) == 2197
    assert row_sum_odd_numbers(19) == 6859
    assert row_sum_odd_numbers(41) == 68921
    assert row_sum_odd_numbers(42) == 74088
    assert row_sum_odd_numbers(74) == 405224
    assert row_sum_odd_numbers(86) == 636056
    assert row_sum_odd_numbers(93) == 804357
    assert row_sum_odd_numbers(101) == 1030301

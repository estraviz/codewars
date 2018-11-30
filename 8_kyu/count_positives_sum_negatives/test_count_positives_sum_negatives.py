from count_positives_sum_negatives import count_positives_sum_negatives


def test_count_positives_sum_negatives():
    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    assert count_positives_sum_negatives(input_array) == [10, -65]

    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    assert count_positives_sum_negatives(input_array) == [10, -65]

    input_array = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
    assert count_positives_sum_negatives(input_array) == [8, -50]

    input_array = [1]
    assert count_positives_sum_negatives(input_array) == [1, 0]

    input_array = [-1]
    assert count_positives_sum_negatives(input_array) == [0, -1]

    input_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert count_positives_sum_negatives(input_array) == [0, 0]

    input_array = []
    assert count_positives_sum_negatives(input_array) == []

from merge_arrays import merge_arrays


def test_merge_arrays_arr1_and_arr2_in_asc_order():
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_arrays(arr1, arr2) == arr3

    arr1 = [10, 8, 6, 4, 2]
    arr2 = [9, 7, 5, 3, 1]
    arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert merge_arrays(arr1, arr2) == arr3

    arr1 = [-20, 35, 36, 37, 39, 40]
    arr2 = [-10, -5, 0, 6, 7, 8, 9, 10, 25, 38, 50, 62]
    arr3 = [-20, -10, -5, 0, 6, 7, 8, 9, 10, 25, 35, 36, 37, 38, 39, 40, 50,
            62]
    assert merge_arrays(arr1, arr2) == arr3


def test_merge_arrays_with_arr1_and_arr2_with_different_lengths():
    arr1 = [5, 6, 7, 8, 9, 10]
    arr2 = [20, 18, 15, 14, 13, 12, 11, 4, 3, 2]
    arr3 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 20]
    assert merge_arrays(arr1, arr2) == arr3

    arr1 = [45, 30, 20, 15, 12, 5]
    arr2 = [9, 10, 18, 25, 35, 50]
    arr3 = [5, 9, 10, 12, 15, 18, 20, 25, 30, 35, 45, 50]
    assert merge_arrays(arr1, arr2) == arr3

    arr1 = [-8, -3, -2, 4, 5, 6, 7, 15, 42, 90, 134]
    arr2 = [216, 102, 74, 32, 8, 2, 0, -9, -13]
    arr3 = [-13, -9, -8, -3, -2, 0, 2, 4, 5, 6, 7, 8, 15, 32, 42, 74, 90, 102,
            134, 216]
    assert merge_arrays(arr1, arr2) == arr3


def test_merge_arrays_with_duplicated_numbers_in_arr1_and_arr2():
    arr1 = [-100, -27, -8, 5, 23, 56, 124, 325]
    arr2 = [-34, -27, 6, 12, 25, 56, 213, 325, 601]
    arr3 = [-100, -34, -27, -8, 5, 6, 12, 23, 25, 56, 124, 213, 325, 601]
    assert merge_arrays(arr1, arr2) == arr3

    arr1 = [18, 7, 2, 0, -22, -46, -103, -293]
    arr2 = [-300, -293, -46, -31, -5, 0, 18, 19, 74, 231]
    arr3 = [-300, -293, -103, -46, -31, -22, -5, 0, 2, 7, 18, 19, 74, 231]
    assert merge_arrays(arr1, arr2) == arr3

    arr1 = [105, 73, -4, -73, -201]
    arr2 = [-201, -73, -4, 73, 105]
    arr3 = [-201, -73, -4, 73, 105]
    assert merge_arrays(arr1, arr2) == arr3

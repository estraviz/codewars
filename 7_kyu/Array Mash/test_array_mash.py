from array_mash import array_mash


def test_array_mash():
    assert array_mash([1, 2, 3], ['a', 'b', 'c']) == [1, 'a', 2, 'b', 3, 'c']

    assert array_mash([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']) == \
        [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']

    assert array_mash([1, 1, 1, 1], [2, 2, 2, 2]) == [1, 2, 1, 2, 1, 2, 1, 2]

    assert array_mash([1, 8, 'hello', 'dog'], ['fish', '2', 9, 10]) == \
        [1, "fish", 8, "2", "hello", 9, "dog", 10]

    assert array_mash([None, 4], [None, 'hello']) == [None, None, 4, "hello"]

    assert array_mash([1], [2]) == [1, 2]

    assert array_mash(['h', 'l', 'o', 'o', 'l'],
                      ['e', 'l', 'w', 'r', 'd']) == \
        ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]

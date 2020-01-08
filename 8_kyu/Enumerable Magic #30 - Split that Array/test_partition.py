from partition import partition


def test_partition_classifier_methods_asks_for_length():
    animals = ["cat", "dog", "duck", "cow", "donkey"]
    assert partition(animals, lambda x: len(x) == 3) == (['cat', 'dog', 'cow'],
                                                         ['duck', 'donkey'])


def test_partition_classifier_methods_asks_for_a_first_character():
    animals = ["cat", "dog", "duck", "cow", "donkey"]
    assert partition(
        animals, lambda x: x[0] == 'c') == (['cat',
                                             'cow'], ['dog', 'duck', 'donkey'])


def test_partition_entry_array_is_empty():
    assert partition([], lambda x: len(x) == 3) == ([], [])

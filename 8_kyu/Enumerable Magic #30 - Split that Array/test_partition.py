from partition import partition


def test_partition():
    animals = ["cat", "dog", "duck", "cow", "donkey"]
    assert partition(animals, lambda x: len(x) == 3) == (['cat', 'dog', 'cow'],
                                                         ['duck', 'donkey'])

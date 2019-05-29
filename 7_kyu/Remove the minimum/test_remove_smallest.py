from numpy.random import randint
from remove_smallest import remove_smallest


def test_simple_ones():
    assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
    assert remove_smallest([1, 2, 3, 4]) == [2, 3, 4]
    assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
    assert remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
    assert remove_smallest([]) == []


def randlist():
    return list(randint(400, size=randint(1, 10)))


def test_returns_empty_list_if_only_one_element():
    for i in range(10):
        x = randint(1, 400)
        assert remove_smallest([x]) == []


def test_returns_list_that_misses_only_one_element():
    for i in range(10):
        arr = randlist()
        assert len(remove_smallest(arr[:])) == len(arr) - 1

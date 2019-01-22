from add_extra import add_extra
from random import randint


def test_add_extra_simple():
    assert add_extra([1, 2]) == [1, 2, 2]
    assert add_extra(['a', 2, 'c', 4, 'e']) == ['a', 2, 'c', 4, 'e', 5]
    assert add_extra([]) == [0]


def test_add_extra_random():
    for _ in range(100):
        myList = [randint(0, 100) for _ in range(randint(1, 4))]
        assert add_extra(myList) == myList + [len(myList)]

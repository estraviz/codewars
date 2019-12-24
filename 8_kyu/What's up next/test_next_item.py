from next_item import next_item
import itertools


def test_simple_tests():
    assert next_item([1, 2, 3, 4, 5, 6, 7, 8], 5) == 6
    assert next_item(['a', 'b', 'c'], 'd') is None
    assert next_item(['a', 'b', 'c'], 'c') is None
    assert next_item('testing', 't') == 'e'
    assert next_item('Hello!', 'o') == '!'


def test_interesting_tests():
    assert next_item(iter(range(1, 30000)), 12) == 13
    assert next_item(iter(itertools.count(3)), 700) == 701

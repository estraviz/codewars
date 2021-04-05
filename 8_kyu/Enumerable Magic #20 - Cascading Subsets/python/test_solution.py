import pytest

from solution import each_cons


lst = [3, 5, 8, 13]


def test_should_return_cascading_lists_of_1_element():
    assert each_cons(lst, 1) == [[3], [5], [8], [13]]


def test_should_return_cascading_lists_of_2_elements():
    assert each_cons(lst, 2) == [[3, 5], [5, 8], [8, 13]]


def test_should_return_cascading_lists_of_3_elements():
    assert each_cons(lst, 3) == [[3, 5, 8], [5, 8, 13]]


def test_empty_list_should_return_an_empty_list():
    assert each_cons([], 3) == []

import pytest

from solution import guess_gifts


def test_guess_test():
    wishlist = [
        {'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
        {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
        {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}
    ]
    presents = [
        {'size': "medium", 'clatters': "a bit", 'weight': "medium"},
        {'size': "small", 'clatters': "yes", 'weight': "light"}
    ]
    assert sorted(guess_gifts(wishlist, presents)) == sorted(['toy car', 'mini puzzle'])

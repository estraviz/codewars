from baubles_on_tree import baubles_on_tree


def test_baubles_on_trees():
    assert baubles_on_tree(5, 5) == [1, 1, 1, 1, 1]
    assert baubles_on_tree(
        5, 0) == "Grandma, we will have to buy a Christmas tree first!"
    assert baubles_on_tree(6, 5) == [2, 1, 1, 1, 1]
    assert baubles_on_tree(50, 9) == [6, 6, 6, 6, 6, 5, 5, 5, 5]
    assert baubles_on_tree(0, 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

from solution import add


def test_add():
    add_one = add(1)
    add_three = add(3)

    assert add_one(3) == 4
    assert add_three(3) == 6
    assert add(1)(3) == 4
    assert add(0)(-15) == -15
    assert add_three(5) == 8
    assert add_three(5) == 8

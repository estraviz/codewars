from solution import compose


def test_compose():
    add1 = lambda a: a + 1
    min1 = lambda a: a - 1
    div2 = lambda a: a / 2
    add15 = lambda a: a + 15
    this = lambda a: a
    total = lambda *args: sum(args)

    assert compose(add1, this)(0) == 1
    assert compose(add1, div2)(2) == 2
    assert compose(add1, total)(1, 2, 3, 4, 5) == 16
    assert compose(add15, this)(0) == 15
    assert compose(this, add15)(0) == 15

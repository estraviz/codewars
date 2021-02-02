from solution import compose


def test_compose():
    f = lambda a: a + 1
    g = lambda a: a
    assert compose(f, g)(0) == 1

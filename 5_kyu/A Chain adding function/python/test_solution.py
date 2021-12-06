from solution import add


def test_chain_adding():
    assert add(1) == 1
    assert add(1)(2) == 3
    assert add(1)(2)(3) == 6
    assert add(1)(2)(3)(4) == 10
    assert add(1)(2)(3)(4)(5) == 15

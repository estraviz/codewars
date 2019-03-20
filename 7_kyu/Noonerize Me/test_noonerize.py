from noonerize import noonerize


def test_noonerize():
    assert noonerize([12, 34]) == 18
    assert noonerize([55, 63]) == 12
    assert noonerize([357, 579]) == 178
    assert noonerize([1000000, 9999999]) == 7000001
    assert noonerize([1000000, "hello"]) == "invalid array"
    assert noonerize(["pippi", 9999999]) == "invalid array"
    assert noonerize(["pippi", "hello"]) == "invalid array"
    assert noonerize([1, 1]) == 0
    assert noonerize([1, 0]) == 1
    assert noonerize([0, 1]) == 1

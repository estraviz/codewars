from solve import solve


def test_solve():
    assert solve("abcdeabcd") == 4
    assert solve("abcd") == 0
    assert solve("abcda") == 1
    assert solve("abcdabc") == 3
    assert solve("abcabc") == 3
    assert solve("abcabca") == 1
    assert solve("aaaaa") == 2
    assert solve("aaaa") == 2
    assert solve("aaa") == 1
    assert solve("aa") == 1
    assert solve("a") == 0
    assert solve("acbacc") == 0

from solve import solve


def test_solve():
    assert solve("100*b/y") == "y/b*100"
    assert solve("a+b-c/d*30") == "30*d/c-b+a"
    assert solve("a*b/c+50") == "50+c/b*a"

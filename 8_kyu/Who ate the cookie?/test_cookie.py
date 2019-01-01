from cookie import cookie


def test_cookie():
    assert cookie("Ryan") == "Who ate the last cookie? It was Zach!"
    assert cookie(2.3) == "Who ate the last cookie? It was Monica!"
    assert cookie(26) == "Who ate the last cookie? It was Monica!"
    assert cookie(True) == "Who ate the last cookie? It was the dog!"
    assert cookie("True") == "Who ate the last cookie? It was Zach!"
    assert cookie(False) == "Who ate the last cookie? It was the dog!"
    assert cookie(1.98528462) == "Who ate the last cookie? It was Monica!"

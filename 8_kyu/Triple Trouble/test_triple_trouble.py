from triple_trouble import triple_trouble


def test_triple_trouble():
    assert triple_trouble("aaa", "bbb", "ccc") == "abcabcabc"
    assert triple_trouble("aaaaaa", "bbbbbb", "cccccc") == "abcabcabcabcabcabc"
    assert triple_trouble("burn", "reds", "roll") == "brrueordlnsl"
    assert triple_trouble("Bm", "aa", "tn") == "Batman"
    assert triple_trouble("LLh", "euo", "xtr") == "LexLuthor"

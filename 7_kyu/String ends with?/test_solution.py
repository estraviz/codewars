from solution import ends_with


def test_cases():
    assert ends_with("samurai", "ai") is True
    assert ends_with("sumo", "omo") is False
    assert ends_with("ninja", "ja") is True
    assert ends_with("sensei", "i") is True
    assert ends_with("samurai", "ra") is False
    assert ends_with("abc", "abcd") is False
    assert ends_with("abc", "abc") is True
    assert ends_with("abcabc", "bc") is True
    assert ends_with('ails', 'fails') is False
    assert ends_with('fails', 'ails') is True
    assert ends_with('this', 'fails') is False

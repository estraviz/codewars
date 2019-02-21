from longest import longest


def test_longest():
    s1 = "aretheyhere"
    s2 = "yestheyarehere"
    assert longest(s1, s2) == "aehrsty"

    s1 = "loopingisfunbutdangerous"
    s2 = "lessdangerousthancoding"
    assert longest(s1, s2) == "abcdefghilnoprstu"

    s1 = "inmanylanguages"
    s2 = "theresapairoffunctions"
    assert longest(s1, s2) == "acefghilmnoprstuy"

    s1 = "lordsofthefallen"
    s2 = "gamekult"
    assert longest(s1, s2) == "adefghklmnorstu"

    s1 = "codewars"
    s2 = "codewars"
    assert longest(s1, s2) == "acdeorsw"

    s1 = "agenerationmustconfrontthelooming"
    s2 = "codewarrs"
    assert longest(s1, s2) == "acdefghilmnorstuw"

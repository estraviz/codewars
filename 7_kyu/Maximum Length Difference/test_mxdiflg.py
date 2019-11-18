from mxdiflg import mxdiflg


def test_mxdiflg():
    s1 = [
        "hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt",
        "znnnnfqknaz", "qqquuhii", "dvvvwz"
    ]
    s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
    assert mxdiflg(s1, s2) == 13

    s1 = [
        "ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb",
        "oocccffuucccjjjkkkjyyyeehh"
    ]
    s2 = ["bbbaaayddqbbrrrv"]
    assert mxdiflg(s1, s2) == 10

    s1 = [
        "ccct", "tkkeeeyy", "ggiikffsszzoo", "nnngssddu", "rrllccqqqqwuuurdd",
        "kkbbddaakkk"
    ]
    s2 = [
        "tttxxxxxxgiiyyy", "ooorcvvj", "yzzzhhhfffaaavvvpp",
        "jjvvvqqllgaaannn", "tttooo", "qmmzzbhhbb"
    ]
    assert mxdiflg(s1, s2) == 14

    s1 = []
    s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
    assert mxdiflg(s1, s2) == -1

    s2 = []
    s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
    assert mxdiflg(s1, s2) == -1

    s1 = []
    s2 = []
    assert mxdiflg(s1, s2) == -1

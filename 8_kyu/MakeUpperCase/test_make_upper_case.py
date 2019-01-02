from make_upper_case import make_upper_case


def test_make_upper_case():
    assert make_upper_case("hello") == "HELLO"
    assert make_upper_case("hello world") == "HELLO WORLD"
    assert make_upper_case("hello world !") == "HELLO WORLD !"
    assert make_upper_case("heLlO wORLd !") == "HELLO WORLD !"
    assert make_upper_case("1,2,3 hello world!") == "1,2,3 HELLO WORLD!"

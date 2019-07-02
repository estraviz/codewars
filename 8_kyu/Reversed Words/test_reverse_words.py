from reverse_words import reverse_words


def test_reverse_words():
    assert reverse_words("hello world!") == "world! hello"
    assert reverse_words("yoda doesn't speak like this") == \
        "this like speak doesn't yoda"
    assert reverse_words("foobar") == "foobar"
    assert reverse_words("kata editor") == "editor kata"
    assert reverse_words("row row row your boat") == "boat your row row row"

    text_in = "The greatest victory is that which requires no battle"
    text_out = "battle no requires which that is victory greatest The"
    assert reverse_words(text_in) == text_out

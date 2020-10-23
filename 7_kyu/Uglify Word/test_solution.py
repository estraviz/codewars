import pytest
from solution import uglify_word


@pytest.mark.parametrize(
    "s, s_out",
    [
        ("AAA", "AaA"),
        ("AaA", "AaA"),
        ("BbB", "BbB"),
        ("aaa-bbb-ccc", "AaA-BbB-CcC"),
        ("AaA-BbB-CcC", "AaA-BbB-CcC"),
        ("eeee-ffff-gggg", "EeEe-FfFf-GgGg"),
        ("EeEe-FfFf-GgGg", "EeEe-FfFf-GgGg"),
        ("qwe123asdf456zxc", "QwE123AsDf456ZxC"),
        ("Hello World", "HeLlO WoRlD"),
    ],
)
def test_uglify_word(s, s_out):
    assert uglify_word(s) == s_out

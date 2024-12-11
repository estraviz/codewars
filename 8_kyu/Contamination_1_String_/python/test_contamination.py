from contamination import contamination


def test_contamination():
    assert contamination("abc", "z") == "zzz"
    assert contamination("", "z") == ""
    assert contamination("abc", "") == ""
    assert contamination("_3ebzgh4", "&") == "&&&&&&&&"
    assert contamination("//case", " ") == "      "

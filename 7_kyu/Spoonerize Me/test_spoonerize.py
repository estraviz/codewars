from spoonerize import spoonerize


def test_spoonerize():
    assert spoonerize("not picking") == "pot nicking"
    assert spoonerize("wedding bells") == "bedding wells"
    assert spoonerize("jelly beans") == "belly jeans"
    assert spoonerize("pop corn") == "cop porn"

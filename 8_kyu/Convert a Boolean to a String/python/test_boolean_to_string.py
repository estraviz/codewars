from boolean_to_string import boolean_to_string


def test_boolean_to_string():
    assert boolean_to_string(True) == "True"
    assert boolean_to_string(False) == "False"
    assert boolean_to_string(False) == "False"

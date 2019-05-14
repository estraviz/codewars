from add_binary import add_binary


def test_binary_addition():
    assert add_binary(1, 1) == "10"
    assert add_binary(0, 1) == "1"
    assert add_binary(1, 0) == "1"
    assert add_binary(2, 2) == "100"
    assert add_binary(51, 12) == "111111"
    assert add_binary(5, 9) == "1110"
    assert add_binary(10, 10) == "10100"
    assert add_binary(100, 100) == "11001000"
    assert add_binary(4096, 1) == "1000000000001"
    assert add_binary(0, 2174483647) == "10000001100110111111110010111111"

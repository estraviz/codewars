from calculate_ratio import calculate_ratio


def test_calculate_ratio():
    assert calculate_ratio(0, 0) == "You threw an error"
    assert calculate_ratio(1024, 768) == "4:3"
    assert calculate_ratio(1366, 768) == "683:384"
    assert calculate_ratio(1920, 1080) == "16:9"
    assert calculate_ratio(732, 200) == "183:50"
    assert calculate_ratio(600, 800) == "3:4"
    assert calculate_ratio(600, 600) == "1:1"

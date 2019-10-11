from first_non_repeated import first_non_repeated


def test_first_non_repeated():
    assert first_non_repeated("test") == 'e'
    assert first_non_repeated("teeter") == 'r'
    assert first_non_repeated("1122321235121222") == '5'

from song_decoder import song_decoder


def test_WUB_replaced_by_1_space():
    assert song_decoder("AWUBBWUBC") == "A B C"


def test_multiples_WUB_replaced_by_1_space():
    assert song_decoder("AWUBWUBWUBBWUBWUBWUBC") == "A B C"


def test_remove_heading_or_trailing_spaces():
    assert song_decoder("WUBAWUBBWUBCWUB") == "A B C"

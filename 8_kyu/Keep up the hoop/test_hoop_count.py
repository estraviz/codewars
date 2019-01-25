from hoop_count import hoop_count


def test_hoop_count():
    assert hoop_count(6) == "Keep at it until you get it"
    assert hoop_count(10) == "Great, now move on to tricks"
    assert hoop_count(22) == "Great, now move on to tricks"

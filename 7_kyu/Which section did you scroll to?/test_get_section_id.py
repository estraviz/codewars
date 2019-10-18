from get_section_id import get_section_id


def test_get_section_id():
    assert get_section_id(1, [300, 200, 400, 600, 100]) == 0
    assert get_section_id(299, [300, 200, 400, 600, 100]) == 0
    assert get_section_id(300, [300, 200, 400, 600, 100]) == 1
    assert get_section_id(1599, [300, 200, 400, 600, 100]) == 4
    assert get_section_id(1600, [300, 200, 400, 600, 100]) == -1

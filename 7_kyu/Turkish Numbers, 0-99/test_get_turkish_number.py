from get_turkish_number import get_turkish_number


def test_get_turkish_number():
    assert get_turkish_number(1) == "bir"
    assert get_turkish_number(13) == "on üç"
    assert get_turkish_number(27) == "yirmi yedi"
    assert get_turkish_number(38) == "otuz sekiz"
    assert get_turkish_number(77) == "yetmiş yedi"
    assert get_turkish_number(94) == "doksan dört"

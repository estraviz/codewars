from zipvalidate import zipvalidate


def test_should_return_true_for_valid_postcode():
    assert zipvalidate('198328') is True
    assert zipvalidate('310003') is True
    assert zipvalidate('424000') is True
    assert zipvalidate('142784') is True
    assert zipvalidate('642784') is True


def test_postcode_should_be_six_digits_long():
    assert zipvalidate('111') is False
    assert zipvalidate('1111111') is False
    assert zipvalidate('AA5590') is False


def test_an_empty_string_is_not_a_postcode():
    assert zipvalidate('') is False


def test_postcode_should_be_with_digits_only():
    assert zipvalidate('\n245980') is False
    assert zipvalidate('245980\n') is False
    assert zipvalidate('245980a') is False
    assert zipvalidate('24598a') is False


def test_postcode_should_be_with_digits_only_and_no_spaces():
    assert zipvalidate(' 310587 ') is False


def test_postcode_cant_start_with_0_5_7_8_or_9():
    assert zipvalidate('555555') is False
    assert zipvalidate('775255') is False
    assert zipvalidate('875555') is False
    assert zipvalidate('012345') is False
    assert zipvalidate('968345') is False


def test_postcode_cant_start_with_a_non_digit_character():
    assert zipvalidate('@68345') is False

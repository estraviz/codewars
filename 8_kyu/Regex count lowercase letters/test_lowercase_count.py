from lowercase_count import lowercase_count


def test_lowercase_count_basic_examples():
    assert lowercase_count("abc") == 3
    assert lowercase_count("abcABC123") == 3
    assert lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 3
    assert lowercase_count("") == 0
    assert lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 0
    assert lowercase_count("abcdefghijklmnopqrstuvwxyz") == 26

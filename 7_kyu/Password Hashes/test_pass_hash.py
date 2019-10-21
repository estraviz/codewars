from pass_hash import pass_hash


def test_pass_hash():
    assert pass_hash('password') == '5f4dcc3b5aa765d61d8327deb882cf99'
    assert pass_hash('abc123') == 'e99a18c428cb38d5f260853678922e03'


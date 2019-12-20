from cannons_ready import cannons_ready


def test_cannons_ready():
    a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
    b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}

    assert cannons_ready(a) == 'Fire!'
    assert cannons_ready(b) == 'Shiver me timbers!'

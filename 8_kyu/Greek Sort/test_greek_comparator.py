from greek_comparator import greek_comparator


def test_greek_comparator():
    assert greek_comparator('alpha', 'beta') < 0
    assert greek_comparator('chi', 'chi') == 0
    assert greek_comparator('upsilon', 'rho') > 0

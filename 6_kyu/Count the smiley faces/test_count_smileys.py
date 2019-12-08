from count_smileys import count_smileys


def test_count_smileys():
    assert count_smileys([]) == 0
    assert count_smileys([':D', ':~)', ';~D', ':)']) == 4
    assert count_smileys([':)', ':(', ':D', ':O', ':;']) == 2
    assert count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1

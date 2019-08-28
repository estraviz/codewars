from match_arrays import match_arrays


def test_match_arrays():
    assert match_arrays(['Perl', 'Closure', 'JavaScript'],
                        ['Go', 'C++', 'Erlang']) == 0
    assert match_arrays(['Erlang', 'JavaScript'], ['Go', 'C++', 'Python']) == 0
    assert match_arrays([True, 3, 9, 11, 15], [True, 3, 11]) == 3
